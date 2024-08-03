import os
import sys
import pyvisa
from time import sleep
from math import ceil
import logging
from typing import Optional
from numbers import Number
import pickle
from seq.tst_case import Test

# scope VISA address (when connecting over LAN)
# lsni -v =>
# USB0::0x1AB1::0x04CE::DS1ZC195002598::INSTR
#   --Primary Expert:       NI-VISA 24.0
#   --Model Name:           DS1000Z Series
#   --Serial Number:        DS1ZC195002598
# IP = 'TCPIP0::172.168.1.139::INSTR'
# rm = pyvisa.ResourceManager()
# print(rm)
# print(rm.list_resources())

BASEDIR = os.path.dirname(os.path.abspath(__file__)) + '/'


class ScopeDS1000zSim:
    """
    test example min/max value
    """
    def __init__(self, ip: Optional[str] = '172.168.1.139',
                 prefix: Optional[str] = 'DS1Z',
                 loglevel: Optional[callable] = logging.DEBUG,
                 pass_if: Optional[bool] = True,
                 min_value: Optional[Number] = 999,
                 max_value: Optional[Number] = 1001,
                 retries: Optional[int] = 3,
                 sim_yaml_file: Optional[str] = "sergio_instrument.yaml@sim"
                 ):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(loglevel)
        self.__resource = 'TCPIP::' + ip + '::INSTR'
        self.__prefix = prefix
        self.__retries = retries
        self.__instrument = None
        # Other internal private arguments
        self.__deviceConnected = False
        self.__sim_yaml = BASEDIR + sim_yaml_file

    # make setting as need it before execute test
    def __get_resource(self, attempt: Optional[int] = 0) -> bool:
        if attempt < self.__retries:
            # Get resources
            try:
                rig = None
                rm = pyvisa.ResourceManager(self.__sim_yaml)
                for r in rm.list_resources():
                    if self.__prefix in r:
                        rig = rm.open_resource(r)
                        break
                else:
                    self.__logger.info(f"Connecting over TCP/IP")
                    rig = rm.open_resource(self.__resource,
                                           read_termination='\n',
                                           write_termination="\r\n"
                                           if self.__resource.startswith("ASRL") else "\n"
                                           )
                sleep(0.1)
                self.__instrument = rig
                self.__logger.info(f"device = {self.__instrument.query('*IDN?').strip()}")    
                self.__deviceConnected = True
                return self.__deviceConnected
            except Exception as e:
                # self.__logger.critical(f"critical error during execution of get_resource : {e}")
                pass
        if not self.__instrument and attempt<self.__retries:
            self.__logger.warning ('Could not connect for {} time(s). It will retry'.format(attempt+1))
            if self.__instrument:  # just in case is open
                self.__instrument.close()
            self.__deviceConnected = False
            self.__get_resource(attempt+1)
        return self.__deviceConnected
  
    def get_resource(self, attempt: Optional[int] = 0) -> bool:
        """Method used to connect to the Scope 
        Returns    
            True: successful connected
            False: failed to connect during 1 times or more   
        """
        try: 
            self.__get_resource(attempt)
            if not self.__deviceConnected:
                self.__logger.error('Could not connect and create scope object')
            else:
                self.__logger.info('Created and Connected the scope object')    
            return self.__deviceConnected
        except BaseException as e:
            self.__logger.critical('critical error during execution of get_resource: {}'.format(e))

    # overriding the execute method
    def meas_freq(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            # q = self.__instrument.query(':MEAS:VAVG? CHAN1')
            # q = self.__instrument.query(':MEAS:VMAX? CHAN1')
            # q = self.__instrument.query(':MEAS:VMIN? CHAN1')    
            q = self.__instrument.query(':MEAS:ITEM? FREQ, CHAN1')
            # q = self.__instrument.query(':MEAS:ITEM? PER, CHAN1')
            # q = self.__instrument.query(':MEAS:ITEM? VPP, CHAN1')
            freq = float(q.split()[0])
            readings.append(freq)
            sleep(0.01)
        return sum(readings)/len(readings)

    def meas_period(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:ITEM? PER, CHAN1')
            res = float(q.split()[0])
            readings.append(res)
            sleep(0.01)
        return sum(readings)/len(readings)
    
    def meas_vpp(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:ITEM? VPP, CHAN1')
            res = float(q.split()[0])
            readings.append(res)
        return sum(readings)/len(readings)
    
    def meas_vavg(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VAVG? CHAN1')
            res = float(q.split()[0])
            readings.append(res)
        return sum(readings)/len(readings)

    def meas_vmin(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VMIN? CHAN1')
            res = float(q.split()[0])
            readings.append(res)
        return sum(readings)/len(readings)

    def meas_vmax(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VMAX? CHAN1')
            res = float(q.split()[0])
            readings.append(res)
        return sum(readings)/len(readings)

    def trace_plot(self):
            if self.__instrument:
                self.__instrument.chunk_size = 32  # Each chunk is 20 kilobytes long by default.
                self.__instrument.timeout = 100    # 25 secs
                self.__instrument.write(':WAV:MODE RAW')
                self.__instrument.write(':WAV:SOUR CHAN1')
                self.__instrument.write('WAV:STAR NORM')  # norm is 1
                self.__instrument.write('WAV:STOP NORM')  # norm is 1200
            buff = None
            sw = 0
            try:
                # buffer = self.__instrument.query_binary_values(':WAV:DATA?', datatype='B')
                if self.__instrument:
                    buff = self.__instrument.query_binary_values(':WAV:DATA?', datatype='B')
                    sleep(0.05)
                else:
                    if sw == 0:
                        fp = open('wave_DS1104Z1.trace', 'rb')
                        sw = 1
                    else:
                        fp = open('wave_DS1104Z2.trace', 'rb')
                        sw = 0
                    buff = pickle.load(fp)
                    sleep(0.5)
                    fp.close()
                return buff
            except Exception as e:
                print(e)
            self.close_resource()

    def close_resource(self):
        if self.__instrument:
            self.__instrument.close()


class ScopeDS1000z:
    """
    test example min/max value
    """

    def __init__(self, ip: Optional[str] = '172.168.1.139',
                 prefix: Optional[str] = 'DS1Z',
                 loglevel: Optional[callable] = logging.INFO,
                 pass_if: Optional[bool] = True,
                 min_value: Optional[Number] = 999,
                 max_value: Optional[Number] = 1001,
                 retries: Optional[int] = 3
                 ):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(loglevel)
        self.__resource = 'TCPIP::' + ip + '::INSTR'
        self.__prefix = prefix
        self.__retries = retries
        self.__instrument = None
        # Other internal private arguments
        self.__deviceConnected = False

    # make setting as need it before execute test
    def __get_resource(self, attempt: Optional[int] = 0) -> bool:
        if attempt < self.__retries:
            # Get resources
            try:
                rig = None
                rm = pyvisa.ResourceManager()
                for r in rm.list_resources():
                    if self.__prefix in r:
                        rig = rm.open_resource(r)
                        break
                else:
                    self.__logger.info(f"Connecting over TCP/IP")
                    rig = rm.open_resource(self.__resource)
                sleep(0.1)
                self.__instrument = rig
                self.__logger.info(f"device = {self.__instrument.query('*IDN?').strip()}")
                self.__deviceConnected = True
                return self.__deviceConnected
            except Exception as e:
                # self.__logger.critical(f"critical error during execution of get_resource : {e}")
                pass
        if not self.__instrument and attempt < self.__retries:
            self.__logger.warning('Could not connect for {} time(s). It will retry'.format(attempt + 1))
            if self.__instrument:  # just in case is open
                self.__instrument.close()
            self.__deviceConnected = False
            self.__get_resource(attempt + 1)
        return self.__deviceConnected

    def get_resource(self, attempt: Optional[int] = 0) -> bool:
        """Method used to connect to the Scope
        Returns
            True: successful connected
            False: failed to connect during 1 times or more
        """
        try:
            self.__get_resource(attempt)
            if not self.__deviceConnected:
                self.__logger.error('Could not connect and create scope object')
            else:
                self.__logger.info('Created and Connected the scope object')
            return self.__deviceConnected
        except BaseException as e:
            self.__logger.critical('critical error during execution of get_resource: {}'.format(e))

    # overriding the execute method
    def meas_freq(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            # q = self.__instrument.query(':MEAS:VAVG? CHAN1')
            # q = self.__instrument.query(':MEAS:VMAX? CHAN1')
            # q = self.__instrument.query(':MEAS:VMIN? CHAN1')
            q = self.__instrument.query(':MEAS:ITEM? FREQ, CHAN1')
            # q = self.__instrument.query(':MEAS:ITEM? PER, CHAN1')
            # q = self.__instrument.query(':MEAS:ITEM? VPP, CHAN1')
            v = float(q.split()[0])
            readings.append(v)
            sleep(0.01)
        return sum(readings) / len(readings)

    def meas_period(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:ITEM? PER, CHAN1')
            v = float(q.split()[0])
            readings.append(v)
            sleep(0.01)
        return sum(readings) / len(readings) * 1000

    def meas_vpp(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:ITEM? VPP, CHAN1')
            v = float(q.split()[0])
            readings.append(v)
        return sum(readings) / len(readings)

    def meas_avg(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VAVG? CHAN1')
            v = float(q.split()[0])
            readings.append(v)
        return sum(readings) / len(readings)

    def meas_min(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VMIN? CHAN1')
            v = float(q.split()[0])
            readings.append(v)
        return sum(readings) / len(readings)

    def meas_max(self):
        self.__instrument.chunk_size = 32
        # self.__instrument.timeout = 100000
        readings = []
        for i in range(5):
            q = self.__instrument.query(':MEAS:VMAX? CHAN1')
            v = float(q.split()[0])
            readings.append(v)
        return sum(readings) / len(readings)

# TODO make it work
    def trace_plot(self):
        if self.__instrument:
            self.__instrument.chunk_size = 32  # Each chunk is 20 kilobytes long by default.
            self.__instrument.timeout = 100  # 25 secs
            self.__instrument.write(':WAV:MODE RAW')
            self.__instrument.write(':WAV:SOUR CHAN1')
            self.__instrument.write('WAV:STAR NORM')  # norm is 1
            self.__instrument.write('WAV:STOP NORM')  # norm is 1200
        buff = None
        sw = 0
        try:
            # buffer = self.__instrument.query_binary_values(':WAV:DATA?', datatype='B')
            if self.__instrument:
                buff = self.__instrument.query_binary_values(':WAV:DATA?', datatype='B')
                sleep(0.05)
            else:
                if sw == 0:
                    fp = open('wave_DS1104Z1.trace', 'rb')
                    sw = 1
                else:
                    fp = open('wave_DS1104Z2.trace', 'rb')
                    sw = 0
                buff = pickle.load(fp)
                sleep(0.5)
                fp.close()
            return buff
        except Exception as e:
            print(e)
        self.close_resource()

    def close_resource(self):
        if self.__instrument:
            self.__instrument.close()


# class ScopeDS1000z_FREQ(Test):
#     '''
#     test example min/max value
#     '''
#     def __init__(self, ip = '172.168.1.139',
#                  prefix = 'DS1Z',
#                  loglevel: Optional[callable] = logging.INFO,
#                  pass_if: Optional[bool] = True,
#                  minLimit:Optional[Number] = 999,
#                  maxLimit:Optional[Number] = 1001,
#                  ):
#         super().__init__(
#             nickname = "measFreq",
#             min_value = minLimit,
#             max_value = maxLimit )
#         self.logger = logging.getLogger(self.__class__.__name__)
#         self.__logger.setLevel(loglevel)
#         self.ip = 'TCPIP::' + ip + '::INSTR'
#         self.prefix = prefix
#         self.instrument = None
    
#     #  make setting as need it before execute test
#     def setup(self, is_passing)-> bool:
#         #Get resources 
#         rig = None
#         rm = pyvisa.ResourceManager()
#         for r in rm.list_resources():
#             if self.prefix in r:
#                 rig = rm.open_resource(r)
#                 break
#         else:
#             self.logger.info(f"Connecting over TCP/IP")
#             rig = rm.open_resource(self.ip)
#         self.instrument = rig
#         self.logger.info(f"device = {self.instrument.query('*IDN?').strip()}")    
#         return True

    
#     #  overriding the execute method
#     def execute(self, is_passing):
#         self.instrument.chunk_size = 32
#         # self.instrument.timeout = 100000
#         readings = []
#         for i in range(5):
#             # q = self.instrument.query(':MEAS:VAVG? CHAN1')
#             # q = self.instrument.query(':MEAS:VMAX? CHAN1')
#             # q = self.instrument.query(':MEAS:VMIN? CHAN1')    
#             q = self.instrument.query(':MEAS:ITEM? FREQ, CHAN1')
#             # q = self.instrument.query(':MEAS:ITEM? PER, CHAN1')
#             # q = self.instrument.query(':MEAS:ITEM? VPP, CHAN1')
#             v = float(q.split()[0])
#             # print(v)
#             readings.append(v)
#         return  sum(readings)/len(readings)

#     def teardown(self, is_passing):
#         # again, simulating another long-running process...
#         if self.instrument:
#             self.instrument.close()
#         sleep(0.1)


# # class DS1xxxZ(Thread):
# class wave():
#     def __init__(self, event:Event, trace:pg, ip = '172.168.1.139', prefix = 'DS1Z'):
#         # Thread.__init__(self)
#         self.event = event
#         self.trace = trace
#         self.ip = 'TCPIP::' + ip + '::INSTR'
#         self.prefix = prefix
#         self.rigol_scope = self._get_resource()
#         if self.rigol_scope:
#             print('device=', self.rigol_scope.query('*IDN?'))


#     def _get_resource(self):
#         try:
#             rig = None
#             rm = pyvisa.ResourceManager()
#             for r in rm.list_resources():
#                 if self.prefix in r:
#                     rig = rm.open_resource(r)
#                     break
#             else:
#                 print('Connecting over TCP/IP')
#                 rig = rm.open_resource(self.ip)
#             return rig
#         except BaseException as e:
#             print(e)
    

#     def trace_plot(self, trace:pg, event:Event):
#     # def run(self):
#         with Lock(): 
#             # self.rigol_scope = self._get_resource()
#             # print('device =', self.rigol_scope.query('*IDN?'))
#             if self.rigol_scope:
#                 self.rigol_scope.chunk_size= 32  #Each chunk is 20 kilobytes long by default. 
#                 self.rigol_scope.timeout = 100    #25 secs
#                 self.rigol_scope.write(':WAV:MODE RAW')
#                 self.rigol_scope.write(':WAV:SOUR CHAN1')
#                 self.rigol_scope.write('WAV:STAR NORM')  #norm is 1
#                 self.rigol_scope.write('WAV:STOP NORM')  #norm is 1200
#             # full_buff = []                               #comment
#             sw = 0
#             while event.is_set():
#                 try:
#                     # buffer = self.rigol_scope.query_binary_values(':WAV:DATA?', datatype='B')
#                     if self.rigol_scope:
#                         buff = self.rigol_scope.query_binary_values(':WAV:DATA?', datatype='B')
#                         sleep(0.05)
#                     else:
#                         if sw == 0:
#                             fp = open('wave_DS1104Z1.trace', 'rb')
#                             sw = 1
#                         else:
#                             fp = open('wave_DS1104Z2.trace', 'rb')
#                             sw = 0
#                         buff = pickle.load(fp)
#                         sleep(0.5)
#                         fp.close()
#                 except BaseException as e:
#                     print(e)
#                     continue
#                 try:
#                     trace.setData(buff)
#                 except Exception as e:
#                     print(e)
#                     continue
#                 # full_buff += buff                       #comment
#             # with open("DS1104Z5.trace", "wb") as fp:    #comment
#             #     pickle.dump(full_buff, fp)              #comment
#             # fp.close()                                  #comment
#             print("thread is done = (")
#             self._close_resource() 

#     def _close_resource(self):
#         if self.rigol_scope:
#             self.rigol_scope.close()



# def runScope():
#     app = pg.mkQApp("Scope DS1104Z")
#     pg.PlotWidget().useOpenGL(True)
#     screen = pg.GraphicsLayoutWidget()
#     screen.show()

#     plt = screen.addPlot()
#     plt.addLegend()
#     plt.showGrid(x=True, y=True, alpha=1.0)
#     plt.setYRange(0, 256, padding=0)
#     plt.setXRange(0, 1200, padding=0)
#     trace = plt.plot(pen='r', name='Cal signal') #symbol = 'o'

#     ev = Event()
#     ev.set()

#     scope = wave( trace, ev, '172.168.1.139', 'DS1Z' )

#     scope_Thread = Thread(
#         target = scope.trace_plot,
#         args = (trace, ev)
#     )
#     scope_Thread.start()

#     app.exec()
#     ev.wait()
#     ev.clear()

# # runScope()

# def scope_meas():
#     print('opening scope..')

#     def _get_resource():
#         try:
#             rig = None
#             prefix = 'DS1Z'
#             ip = 'TCPIP::172.168.1.139::INSTR'
#             rm = pyvisa.ResourceManager()
#             for r in rm.list_resources():
#                 if prefix in r:
#                     rig = rm.open_resource(r)
#                     break
#             else:
#                 print('Connecting over TCP/IP')
#                 rig = rm.open_resource(ip)
#             return rig
#         except BaseException as e:
#             print(e)    
#             print('no instrument found :(')
#             return None
        
#     rig = _get_resource()
#     if not rig:
#         return None
#     rig.chunk_size = 32
#     rig.timeout = 3000
#     readings = []
#     for i in range(50):
#         try:
#             # q = rig.query(':MEAS:VAVG? CHAN1')
#             # q = rig.query(':MEAS:VMAX? CHAN1')
#             # q = rig.query(':MEAS:VMIN? CHAN1')    
#             # q = rig.query(':MEAS:ITEM? FREQ, CHAN1')
#             # q = rig.query(':MEAS:ITEM? PER, CHAN1')
#             q = rig.query(':MEAS:ITEM? VPP, CHAN1')
#             v = float(q.split()[0])
#             print(v)
#             readings.append(v)
#         except Exception as e:
#             print(e) 
#             break
#     rig.close()
#     return readings
    
# # x = scope_meas()


# def screenShot():
#     print('opening scope..')

#     def _get_resource():
#         try:
#             rig = None
#             prefix = 'DS1Z'
#             ip = 'TCPIP::172.168.1.139::INSTR'
#             rm = pyvisa.ResourceManager()
#             for r in rm.list_resources():
#                 if prefix in r:
#                     rig = rm.open_resource(r)
#                     break
#             else:
#                 print('Connecting over TCP/IP')
#                 rig = rm.open_resource(ip)
#             return rig
#         except BaseException as e:
#             print(e)    
#             print('no instrument found :(')
#             return None
        
#     rig = _get_resource()
#     if not rig:
#         return None    
         
#     rig.timeout = 3000
#     rig.chunk_size = 32

#     print('device =', rig.query('*IDN?'))
#     sleep(0.1)

#     rig.write(':DISP:DATA? ON,OFF,PNG')
#     sleep(0.1)
#     buff = rig.read_raw()
#     with open("scr2.dat", "wb") as fp:          #comment
#         pickle.dump(buff, fp)                   #comment
#     open('scr2.png', 'wb').write(buff[11:len(buff)-1])

#     rig.close()    
    
# # x = screenShot()

# def screenShot_offline():
#     fp = open('scr2.dat', 'rb')
#     buff = pickle.load(fp)
#     open('scr2off.png', 'wb').write(buff[11:len(buff)-1])

# # x = screenShot_offline()



# ####### power_analysis sim
# def power_analysis():
#     # number of traces to capture
#     TRACES_COUNT = 2

#     # scope VISA address (when connecting over LAN)
#     # ip = 'TCPIP0::169.254.145.64::INSTR'
#     # ip = 'TCPIP0::169.254.125.139::INSTR'
#     ip = 'TCPIP0::172.168.1.139::INSTR'

#     rm = pyvisa.ResourceManager()
#     for r in rm.list_resources():
#         if 'DS1Z' in r:
#             print('Connecting over USB')
#             rig = rm.open_resource(r)
#             break
#     else:
#         print('Connecting over TCP/IP')
#         rig = rm.open_resource(ip)

#     if not rig:
#         print('Scope not found')
#         exit()


#     rig.timeout = 1500
#     rig.chunk_size = 32
#     max_points = 250_000 # safe up to 250k

#     print('device:', rig.query('*IDN?'))
#     rig.write(':WAV:MODE RAW')
#     rig.write(':WAV:FORM BYTE')

#     # mem = int(rig.query(':ACQ:MDEP?'))
#     mem = (rig.write(':ACQuire:MDEPth 12000'))
#     mem = int(rig.query(':ACQuire:MDEPth?'))
#     if max_points > mem: max_points = mem
#     f = open(time.strftime('%b-%d-%Y_%H-%M-%S', time.localtime()) + '_trace.csv', 'w')

#     for trace in range(TRACES_COUNT):
#         # single capture
#         rig.write(':SING')
#         print('waiting for trigger..')
#         time.sleep(0.3) # STOP->WAIT transition takes a while
#         while True:
#             if 'STOP' in rig.query(':TRIG:STAT?'):
#                 break
#             time.sleep(0.1)

#         # deep memory read
#         buf = []
#         for i in range (ceil(mem / max_points)):
#             start = i * max_points
#             stop = start + max_points
#             stop = mem if stop > mem else stop
#             time.sleep(0.01)
#             rig.write(f':WAV:STAR {start + 1}')
#             rig.write(f':WAV:STOP {stop}')

#             for retries in range(10):
#                 try:
#                     tmp = rig.query_binary_values(':WAV:DATA? CH1', datatype='B')
#                     if len(tmp) != stop - start:
#                         print(f'got {len(tmp)}/{stop - start} bytes - retrying')
#                         continue
#                     buf += tmp
#                     break
#                 except:
#                     print('retrying')
#             else:
#                 print('too many retries - quitting')
#                 break
#             print(f'chunk {i}: {len(buf)}')

#         f.write(','.join([str(v) for v in buf]) + '\n')

#     f.close()
#     rig.close()
    
# # power_analysis()

# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import signal
# from scipy.ndimage import shift
# def align():
#     with open('Jul-22-2024_09-47-38_trace.csv', 'r') as f:  
#     # with open('trace.csv', 'r') as f: 
#         # process the first trace
#         a = [int(i) for i in f.readline().split(',')]
#         a -= np.mean(a)
#         averaged_trace = a[:]

#         l = f.readline()
#         n = 0
#         while l:
#             b = [int(i) for i in l.split(',')]
#             b -= np.mean(b)

#             # align using cross-correlation
#             cor = signal.correlate(a, b)
#             px, py = signal.find_peaks(cor, height=0)
#             peak_x = px[np.argmax(py['peak_heights'])]
#             offset = len(a) - peak_x - 1 # a -> b offset
#             b = shift(b, -offset, cval=np.median(b))

#             # moving average
#             averaged_trace = [(b[i] + n*averaged_trace[i])/(n + 1) for i in range(len(b))]

#             n += 1
#             l = f.readline()

#     plt.grid(True)
#     plt.plot(a, alpha=0.9)
#     plt.plot(averaged_trace)
#     plt.show()
    
# align()