import socket
from typing import Optional
import logging
import time
import random


class Lidar:
    def __init__(self,
                 # loglevel: Optional[callable]= logging.INFO,
                 *args, **kwargs):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.CRITICAL)
        # args values
        self.__simulation = args[0][1]
        # kwargs without default values
        # self.__regAddrList= [kwargs['REGPOLYDELAY'], kwargs['REGSMSPOLYDELAY'], \
        #                    kwargs['REGSA'], kwargs['REGSMSSA']]
        self.__regTemp= kwargs['REGTEMPCPU']
        # kwargs with default values
        default_kwargs = {'WHOIAM': 'FALCON',  'HOST': "172.168.1.10", 'PORT': 8001, 'RETRY_ATTEMPTS': 3,
                          'SOCKET_TIMEOUT': 3, 'LOOP_TIMEOUT': 5}
        kwargs = { **default_kwargs, **kwargs }
        self.__host = kwargs['HOST']
        self.__port = kwargs['PORT']
        self.__retries = kwargs['RETRY_ATTEMPTS']
        self.__timeout = kwargs['SOCKET_TIMEOUT']
        # Other internal private arguments
        self.__lidarConnected = False
        self.__socket = None
        self.__RPM = 0
        self.__cycleTime = 0.0
        self.__register_value = None
        self.__temperature_value = None
        self.__sn = "dummy_sn"

    def __connect_lidar(self, attempt: Optional[int] = 0):
        if attempt < self.__retries:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.settimeout(self.__timeout)
            try:
                # class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
                self.__socket.connect((self.__host, self.__port))
                self.__lidarConnected = True
            except socket.error :
                pass
        if not self.__lidarConnected and attempt<self.__retries:
            self.__logger.warning ('Could not connect for {} time(s).'.format(attempt+1))
            self.__connect_lidar(attempt+1)
        return self.__lidarConnected

    def connect_lidar(self):
        """Method used to connect a socket to the lidar 
        socket:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        Returns    
            True: successfully connected
            False: failed to connect during 1 times or more   
        """
        try:
            if self.__simulation:
                self.__lidarConnected = True
            else:
                self.__connect_lidar(0)
            if not self.__lidarConnected:
                self.__logger.error('Could not connect and create lidar object')
            else:
                self.__logger.info('Created and Connected the lidar object')
            return self.__lidarConnected
        except BaseException as e:
            self.__logger.error('The falcon connect_lidar exception: {}'.format(e))

    def read_rpm(self):
        # if (self.__simulation == True ): return float(1/ float(5400 / 60) )
        if self.__simulation:
            return 5400
        breg_adds= bytes('get_i_config motor mtr_f_rpm', 'utf-8')
        self.__socket.sendall(breg_adds)
        received = str(self.__socket.recv(1024), "utf-8").split()
        self.__RPM = int (received[len(received)-1])           # RPM
        self.__cycleTime = float(1/ float(self.__RPM / 60) )     # sec
        return self.__RPM

    def __read_sn(self, **kwargs ):
        if self.__simulation:
            return '371182210154'
        # kwargs with default values
        default_kwargs = {'regName':'get_sn'}
        kwargs = {**default_kwargs, **kwargs}
        reg_name= kwargs['regName']
        breg_adds= bytes(reg_name, 'utf-8')
        self.__socket.sendall(breg_adds)
        received = str(self.__socket.recv(1024), "utf-8").split()
        return received[len(received) - 1]  # Serial

    def get_sn(self):
        """Method used to get falcon serial number 
        Returns    
            falcon serial number 
        """
        try:
            self.__sn = self.__read_sn()
            return self.__sn
        except BaseException as e:
            self.__logger.error('The falcon get serial number exception: {}'.format(e))

    def __read_temp_cpu(self, reg_temp):
        # if( self.__simulation == True ): return regTemp + ' ' + hex( int(self.__random_value(60, 2)) )
        if self.__simulation:
            return  int(self.__random_value(60, 2))
        breg_adds= bytes('get_cpu_temp', 'utf-8')
        self.__socket.sendall(breg_adds)
        received = str(self.__socket.recv(1024), "utf-8").split()   # Temperature CPU
        # return reg_temp + ' ' + hex( int (received[len(received)-1]) )
        return int(received[len(received)-1])

    def get_temperature_cpu(self):
        """Method used to read the falcon lidar temeprature 
        Returns    
            The hex value of the temperature in celciuos
        """
        try:
            self.__temperature_value = self.__read_temp_cpu(self.__regTemp)
            return self.__temperature_value
        except BaseException as e:
            self.__logger.error('The falcon get CPU temperature exception: {}'.format(e))

    def __read_reg(self, reg_addr):  # 'reg_rd: 0x330 0x13'
        # if( self.__simulation == True ):  return regAddr + ' ' + hex( int(self.__random_value(81062, 4)) )
        if self.__simulation:
            return 'reg_rd: ' + reg_addr + ' ' + hex( int(self.__random_value(81062, 4)) )
        breg_addr = bytes('reg_rd ' + reg_addr, 'utf-8')
        self.__socket.sendall(breg_addr)   # self.__socket.sendall(b'reg_rd 0x328')
        return str(self.__socket.recv(1024), "utf-8")

    def read_regpl(self, reg_addr):
        """Method used to read to a Flacon lidar register 
        args:
            regAddr:  Address of the register to read
            value:  Values read from the register
        Returns    
            The value read from teh register
        """
        try:
            time.sleep(0.001)
            self.__register_value= self.__read_reg(reg_addr)
            return self.__register_value
        except BaseException as e:
            self.__logger.error('The falcon readRegPl exception: {}'.format(e))
            print('ERROR: The falcon readRegPl  exception: {}'.format(e))

    def __write_reg(self, reg_addr, value):
        breg_addr_value= bytes('reg_wr ' + reg_addr + ' ' + value, 'utf-8')
        self.__socket.sendall(breg_addr_value)

    def write_regpl(self, reg_addr, value):
        """Method used to write to a Flacon lidar register 
        args:
            regAddr:  Address of the register to write
            value:  Values to write on the register
        Returns    
            The reading of the value wrote on the Register
        """
        try:
            # if( self.__simulation == True ): return self.__random_value(81062, 4)?
            if self.__simulation:
                return value
            self.__write_reg(reg_addr, value)
            time.sleep(0.002)
            self.__register_value= self.__read_reg(reg_addr)
            return self.__register_value
        except BaseException as e:
            print('ERROR: The falcon write_regpl  exception: {}'.format(e))
            self.__logger.error('The falcon write_regpl exception: {}'.format(e))

    def __random_value(self, val, var):
        res = round(random.uniform((val-var), (val+var)), 3)
        return res