import os
from pathlib import Path
from time import sleep 
from seq.tst_sequence import TestSequence, Test
from random import choice, random
# from threading import Thread, Semaphore
from scope_DS1000Z_sim import Scope_DS1000Z
from lidar import Lidar
import configparser


# config initialization data
config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent   # Figures out the absolute path
initFile=  os.path.join(BASE_DIR, 'config.ini')
config.read(initFile)
SIM= False
args = ( config.get('APP', 'VERSION'), SIM )


class TestProd_1(Test):
    '''
    test example P/F
    '''
    def __init__(self):
        super().__init__(
            nickname= "test_1",
            pass_if=True )
        return
    
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True
    
    #  overriding the execute method
    def execute(self, is_passing):
        return choice([True] * 3 + [False])

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class TestProd_2(Test):
    '''
    test example min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "test_2",
            min_value= 7.2,
            max_value=7.8 )
        return
    
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True
    
    #  overriding the execute method
    def execute(self, is_passing):
        result = 7.5 + random()
        return result
    
    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class Scope_DS1000Z_instrument(Scope_DS1000Z):
    def __init__(self):
        scope= super().__init__(
            IP='172.168.1.139', 
            prefix='DS1Z',  
        )
        return scope

class Scope_DS1000Z_get_resource(Test):
    '''
    test example min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Scope_DS1000Z_get_resource",
            pass_if=True )
        self.scope= Scope_DS1000Z_instrument()
    
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.scope.get_resource()
        return res
    
    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()
        sleep(0.1)
        


class Scope_DS1000Z_meas_freq(Test):
    '''
    test example min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Scope_DS1000Z_meas_freq",
            min_value= 995,
            max_value= 1005 )
        self.scope= Scope_DS1000Z_instrument()
    
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.scope.get_resource()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.scope.meas_freq()
        return res
    
    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()
 
 
class Scope_DS1000Z_meas_period(Test):
    '''
    test example min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Scope_DS1000Z_meas_period",
            min_value= 0.995,
            max_value= 1.005 )
        self.scope= Scope_DS1000Z_instrument()
    
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.scope.get_resource()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.scope.meas_period()
        return res
    
    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()
               
        
class Lidar_system(Lidar):
    def __init__(self):
        lidar_conecction= super().__init__( args,
            REGTEMPCPU= config.get("REG", "REGTEMPCPU" ),
            #kwargs with default values
            HOST= config.get("APP", "HOST" ),
            PORT= config.getint("APP", "PORT"),
            RETRY_ATTEMPTS= config.getint("APP", "RETRY_ATTEMPTS"),
            SOCKET_TIMEOUT= config.getint("APP", "SOCKET_TIMEOUT"),
        )
        return lidar_conecction
           
class Lidar_conecction(Test):
    '''
    test case Pass/Fail
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_conecction",
            pass_if=True )
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class Lidar_temperature(Test):
    '''
    test case min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_temperature",
            min_value= 20,
            max_value=70 )
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.lidar_conecction.getTempCPU()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class Lidar_getSN(Test):
    '''
    test case min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_getSN",
            pass_if='371182210154' )
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.lidar_conecction.getSN()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class Lidar_readPRM(Test):
    '''
    test case min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_readPRM",
            pass_if=5400 )
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        res= self.lidar_conecction.readPRM()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class Lidar_readRegPl(Test):
    '''
    test case min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_readRegPl",
            pass_if= True)
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        reg= config.get("REG", "REGPOLYDELAY")
        regVal= self.lidar_conecction.readRegPl(reg)
        res= regVal.startswith('reg_rd: 0x330 0x13') #'reg_rd: 0x330 0x13c07\n'
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

class Lidar_writeRegPl(Test):
    '''
    test case min/max value
    '''
    def __init__(self):
        super().__init__(
            nickname= "Lidar_writeRegPl",
            pass_if= True)
        self.lidar_conecction = Lidar_system()
        
    #  make setting as need nbefore execute test
    def setup(self, is_passing):
        res= self.lidar_conecction.connectLidar()
        return res
    
    #  overriding the execute method
    def execute(self, is_passing):
        reg= config.get("REG", "REGSARATE")
        self.lidar_conecction.writeRegPl(reg, '0x200')
        regVal= self.lidar_conecction.readRegPl(reg)
        res1= regVal.startswith('reg_rd: 0x328 0x200\n') 
        # return res
        self.lidar_conecction.writeRegPl(reg, '0x100')
        regVal= self.lidar_conecction.readRegPl(reg)
        res2= regVal.startswith('reg_rd: 0x328 0x100\n') 
        return res1 and res2

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)

#TODO        
class TestPlan():
    def __init__(self):
        return

    def execute(self):
        return True

        
def main():    
    sequence= [ TestProd_1(), 
                TestProd_2(),
                Scope_DS1000Z_get_resource(),
                Scope_DS1000Z_meas_freq(), 
                Scope_DS1000Z_meas_period(),
                Lidar_conecction(),
                Lidar_temperature(),
                Lidar_getSN(),
                Lidar_readPRM(),
                Lidar_readRegPl(),
                Lidar_writeRegPl()
               ]
    ts= TestSequence(sequence= sequence,
                     auto_run=False)
    # ts2= TestSequence(sequence= sequence,
    #                  auto_run=False)  
    for x in range(1):
        ts.startTests()
        while ts.get_state != "complete / ready" :
            sleep(1)
        # ts2.startTests()
        # sleep(0.5)

    # # semaphore= Semaphore(2) 
    # # fts= Thread(target=ts._run_sequence, daemon=True, args=(semaphore))
    # # fts.daemon= True
    # ts.start()
    # for x in range(3):
    #     ts._start()
    #     sleep(0.5)
    #     # ts.join()
    

if __name__ == "__main__":
    main()