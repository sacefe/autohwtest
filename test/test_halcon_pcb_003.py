import os
import pytest
import configparser
from inst_uut_tstcases.tst_halcon_pcb_003 import HalconPcbPn003

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
initFile = BASEDIR + "/inst_uut_tstcases/config.ini"
config.read(initFile)


class TestTstHalconPcbPn003:
    @pytest.fixture
    def obj_tstHalconPcbPn003(self):
        return HalconPcbPn003()

    @pytest.mark.parametrize("sn", [
        '371182210154'
    ])
    def test_get_sn(self, obj_tstHalconPcbPn003, sn):
        serial = obj_tstHalconPcbPn003.read_product_sn()
        assert serial == sn

    PERIOD= pytest.mark.parametrize("expected", [
        0.0111
    ])

    @PERIOD
    def test_get_lidar_rpm_period(self, obj_tstHalconPcbPn003, expected):
        rpm_period = obj_tstHalconPcbPn003.get_lidar_rpm_period()
        assert rpm_period == expected

    @PERIOD
    def test_get_scope_rpm_period(self, obj_tstHalconPcbPn003, expected):
        rpm_period = obj_tstHalconPcbPn003.get_scope_rpm_period()
        assert rpm_period == expected

    def test_compare_rpm_period(self, obj_tstHalconPcbPn003):
        result = obj_tstHalconPcbPn003.compare_rpm_period()
        assert result == True


pytest.main(['-v'])
