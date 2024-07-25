import socket
from typing import Optional
import logging
import coloredlogs
import time
import random

coloredlogs.install(level="INFO")

class Lidar:
    def __init__(self, 
                #  loglevel: Optional[callable]= logging.INFO,
                 *args, **kwargs): 
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.INFO)
        #args values
        self.__simulation = args[0][1]
        #kwargs without default values
        #self.__regAddrList= [kwargs['REGPOLYDELAY'], kwargs['REGSMSPOLYDELAY'], \
        #                    kwargs['REGSA'], kwargs['REGSMSSA']]
        self.__regTemp= kwargs['REGTEMPCPU']  
        #kwargs with default values
        defaultKwargs = { 'WHOIAM':'FALCON',  'HOST':"172.168.1.10", 'PORT':8001, 'RETRY_ATTEMPTS':3,\
                            'SOCKET_TIMEOUT':3, 'LOOP_TIMEOUT':5}
        kwargs = { **defaultKwargs, **kwargs }
        self.__host = kwargs['HOST']
        self.__port = kwargs['PORT']
        self.__retrys= kwargs['RETRY_ATTEMPTS']
        self.__timeout= kwargs['SOCKET_TIMEOUT']
        # Other internal private arguments
        self.__lidarConnected = False
        self.__socket = None
        self.__RPM = 0
        self.__cycleTime = 0.0

                
    def __connectLidar(self, attempt:Optional[int]= 0):
        if attempt<self.__retrys:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.__socket.settimeout(self.__timeout)
            try:
                #class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
                self.__socket.connect((self.__host, self.__port))
                self.__lidarConnected = True
            except socket.error :
                pass
        if not self.__lidarConnected and attempt<self.__retrys: 
            self.__logger.warning ('Could not connect for {} time(s).'.format(attempt+1))
            self.__connectLidar(attempt+1)
        return self.__lidarConnected
    
    def connectLidar(self):
        """Method used to connect a socket to the lidar 
        socket:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        Returns    
            True: sucessluffy conected 
            False: failed to connect during 1 times or more   
        """
        try: 
            if (self.__simulation == True ): self.__lidarConnected= True
            else: self.__connectLidar(0)
            if not self.__lidarConnected:
                self.__logger.error('Could not connect and create lidar object')
            else:
                self.__logger.info('Created and Connected the lidar object')    
            return self.__lidarConnected
        except BaseException as e:
            self.__logger.error('The falcon connectLidar exception: {}'.format(e))
            
            
    def readPRM(self):
        if (self.__simulation == True ): return float(1/ float(5400 / 60) )
        bregAadds= bytes('get_i_config motor mtr_f_rpm', 'utf-8')
        self.__socket.sendall(bregAadds)
        received = str(self.__socket.recv(1024), "utf-8").split()
        self.__RPM = int (received[len(received)-1])           # RPM
        self.__cycleTime = float(1/ float(self.__RPM / 60) )     # sec
        return self.__RPM
    
    def __readSN(self, **kwargs ):
        if( self.__simulation == True ): return 'serialDummy'  
        #kwargs with default values
        defaultKwargs = { 'regName':'get_sn' }
        kwargs = { **defaultKwargs, **kwargs }
        regName= kwargs['regName']       
        bregAadds= bytes(regName, 'utf-8')
        self.__socket.sendall(bregAadds)
        received = str(self.__socket.recv(1024), "utf-8").split()
        return  (received[len(received)-1])           # Serial
    
    
    def getSN(self):
        """Method used to get falcon serial number 
        Returns    
            falcon serial number 
        """
        try: 
            self.__SN= self.__readSN()
            return self.__SN
        except BaseException as e:
            self.__logger.error('The falcon get serial number exception: {}'.format(e))
            
    
    def __readTempCPU(self, regTemp):
        if( self.__simulation == True ): return regTemp + ' ' + hex( int(self.__randomValue(60, 2)) )      
        bregAadds= bytes('get_cpu_temp', 'utf-8')
        self.__socket.sendall(bregAadds)
        received  = str(self.__socket.recv(1024), "utf-8").split()   #Temperature CPU
        # return regTemp + ' ' + hex( int (received[len(received)-1]) ) 
        return  int (received[len(received)-1]) 


    def getTempCPU(self):
        """Method used to read the falcon lidar temeprature 
        Returns    
            The hex value of the temperature in celciuos
        """  
        try: 
            self.__TemperatureValue= self.__readTempCPU(self.__regTemp)
            return self.__TemperatureValue  
        except BaseException as e:
            self.__logger.error('The falcon get CPU temperature exception: {}'.format(e))
           
            
    def __readReg(self, regAddr):
        if( self.__simulation == True ):  return regAddr + ' ' + hex( int(self.__randomValue(81062, 4)) )
        bregAaddr= bytes('reg_rd ' + regAddr, 'utf-8')
        self.__socket.sendall(bregAaddr)   # self.__socket.sendall(b'reg_rd 0x328')  
        return str(self.__socket.recv(1024), "utf-8")
    
    def readRegPl(self, regAddr):
        """Method used to read to a Flacon lidar register 
        args:
            regAddr:  Address of the register to read
            value:  Values read from the register
        Returns    
            The value read from teh register
        """   
        try: 
            time.sleep(0.001)
            self.__registerValue= self.__readReg(regAddr)
            return self.__registerValue   
        except BaseException as e:
            self.__logger.error('The falcon readRegPl exception: {}'.format(e))
            print('ERROR: The falcon readRegPl  exception: {}'.format(e))


    def __writeReg(self, regAddr, value):
        bregAaddrValue= bytes('reg_wr ' + regAddr + ' ' + value, 'utf-8')
        self.__socket.sendall(bregAaddrValue)

    def writeRegPl(self, regAddr, value):
        """Method used to write to a Flacon lidar register 
        args:
            regAddr:  Address of the register to write
            value:  Values to write on the register
        Returns    
            The reading of the value wrote on the Register
        """  
        try:     
            if( self.__simulation == True ): return self.__randomValue(81062, 4)
            self.__writeReg(regAddr, value)
            time.sleep(0.002)
            self.__registerValue= self.__readReg(regAddr)
            return self.__registerValue 
        except BaseException as e:
            print('ERROR: The falcon writeRegPl  exception: {}'.format(e))
            self.__logger.error('The falcon writeRegPl exception: {}'.format(e))
            
    def __randomValue(self, val, var):
        res= round(random.uniform((val-var), (val+var)), 3)
        return res