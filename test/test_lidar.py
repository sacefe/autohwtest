import os
from pathlib import Path
import pytest

# BASE_DIR = Path(__file__).resolve().parent.parent   # Figures out the absolute path
# sys.path.append(BASE_DIR  )
from lidar import Lidar
import configparser


# config initialization data
config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent   # Figures out the absolute path
initFile=  os.path.join(BASE_DIR, 'config.ini')
config.read(initFile)
SIM= False
args = ( config.get('APP', 'VERSION'), SIM )
    
    
class Test_Lidar():
    @pytest.fixture
    def lidarObj(self):
        return Lidar( args,
            REGTEMPCPU= config.get("REG", "REGTEMPCPU" ),
            #kwargs with default values
            HOST= config.get("APP", "HOST" ),
            PORT= config.getint("APP", "PORT"),
            RETRY_ATTEMPTS= config.getint("APP", "RETRY_ATTEMPTS"),
            SOCKET_TIMEOUT= config.getint("APP", "SOCKET_TIMEOUT"),
        )
        
    def test_connectLidar(self, lidarObj):
        assert lidarObj.connectLidar() == True   

    @pytest.mark.parametrize("rpm",[
        (5400)
    ])    
    def test_readPRM(self, lidarObj, rpm):
        lidarObj.connectLidar()
        rpm= lidarObj.readPRM()
        assert rpm == 5400
        
    @pytest.mark.parametrize("sn",[
        ('371182210154')
    ])    
    def test_getSN(self, lidarObj, sn):
        lidarObj.connectLidar()
        serial= lidarObj.getSN()
        assert serial == sn
    
    @pytest.mark.parametrize("expected_temperature",[
        ({'temp_range_c':[20,70]} )
    ])       
    def test_getTempCPU(self, lidarObj, expected_temperature):
        lidarObj.connectLidar()
        min= expected_temperature.get('temp_range_c')[0]
        max= expected_temperature.get('temp_range_c')[1]
        temperature= lidarObj.getTempCPU()
        assert temperature > min
        assert temperature < max
    
    @pytest.mark.parametrize("register_str",[
        ('reg_rd: 0x330 0x13')
    ])        
    def test_readRegPl(self, register_str, lidarObj):
        lidarObj.connectLidar()
        reg= config.get("REG", "REGPOLYDELAY")
        regVal= lidarObj.readRegPl(reg)
        assert regVal.startswith(register_str) #'reg_rd: 0x330 0x13c07\n'

    @pytest.mark.parametrize("register_str",[
        ({'reg_rd':[config.get("REG", "REGSARATE"), 
                    '0x200','reg_rd: 0x328 0x200\n']} ),
        ({'reg_rd':[config.get("REG", "REGSARATE"),
                    '0x100','reg_rd: 0x328 0x100\n']} )
    ])  
    def test_writeRegPl(self, register_str, lidarObj):
        lidarObj.connectLidar()
        reg= register_str.get('reg_rd')[0]
        value= register_str.get('reg_rd')[1]
        str_ret=  register_str.get('reg_rd')[2]
        regVal= lidarObj.writeRegPl(reg, value) #(reg, '0x200')
        regVal= lidarObj.readRegPl(reg)
        assert regVal.startswith(str_ret) 


