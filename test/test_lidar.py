import os
import pytest
import configparser
from inst_uut_tstcases.lidar import Lidar


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
initFile = BASEDIR + "/examples/testplans/local.ini"
config.read(initFile)

SIM = True
args = (config.get('APP', 'VERSION'), SIM)


class TestLidar:
    @pytest.fixture
    def lidar_obj(self):
        return Lidar(args,
                     REGTEMPCPU=config.get("REG", "REGTEMPCPU"),
                     # kwargs with default values
                     HOST=config.get("APP", "HOST"),
                     PORT=config.getint("APP", "PORT"),
                     RETRY_ATTEMPTS=config.getint("APP", "RETRY_ATTEMPTS"),
                     SOCKET_TIMEOUT=config.getint("APP", "SOCKET_TIMEOUT"),
                     )

    def test_connect_lidar(self, lidar_obj):
        assert lidar_obj.connect_lidar() == True

    @pytest.mark.parametrize("rpm", [
        5400
    ])
    def test_read_rpm(self, lidar_obj, rpm):
        lidar_obj.connect_lidar()
        rpm = lidar_obj.read_rpm()
        assert rpm == 5400

    @pytest.mark.parametrize("sn", [
        '371182210154'
    ])
    def test_get_sn(self, lidar_obj, sn):
        lidar_obj.connect_lidar()
        serial = lidar_obj.get_sn()
        assert serial == sn

    @pytest.mark.parametrize("expected_temperature", [
        ({'temp_range_c': [20, 70]})
    ])
    def test_get_cpu_temp(self, lidar_obj, expected_temperature):
        lidar_obj.connect_lidar()
        minvalue = expected_temperature.get('temp_range_c')[0]
        maxvalue = expected_temperature.get('temp_range_c')[1]
        temperature = lidar_obj.get_temperature_cpu()
        assert temperature > minvalue
        assert temperature < maxvalue

    @pytest.mark.parametrize("register_str", [
        'reg_rd: 0x330 0x13'
    ])
    def test_read_regpl(self, register_str, lidar_obj):
        lidar_obj.connect_lidar()
        reg = config.get("REG", "REGPOLYDELAY")
        regVal = lidar_obj.read_regpl(reg)
        assert regVal.startswith(register_str)  # 'reg_rd: 0x330 0x13c07\n'

    @pytest.mark.parametrize("register_str", [
        ({'reg_rd': [config.get("REG", "REGSARATE"),
                     '0x200', 'reg_rd: 0x328']}),
        # '0x200','reg_rd: 0x328 0x200\n']} ),
        ({'reg_rd': [config.get("REG", "REGSARATE"),
                     '0x100', 'reg_rd: 0x328']})
        # '0x100','reg_rd: 0x328 0x100\n']} )
    ])
    def test_write_regpl(self, register_str, lidar_obj):
        lidar_obj.connect_lidar()
        reg = register_str.get('reg_rd')[0]
        value = register_str.get('reg_rd')[1]
        str_ret = register_str.get('reg_rd')[2]
        lidar_obj.write_regpl(reg, value)  # (reg, '0x200')
        reg_val = lidar_obj.read_regpl(reg)
        assert reg_val.startswith(str_ret)


pytest.main(['-v'])
