from __init__ import *
import pytest
from inst_uut_tstcases.scope_DS1000Z_sim import ScopeDS1000z, ScopeDS1000zSim
import sys
import os


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)


class TestScopeDS1000Z:

    @pytest.fixture
    def scope_obj(self):
        return ScopeDS1000zSim(
            ip='172.168.1.139',
            prefix='DS1Z',
            sim_yaml_file=BASEDIR + "\\inst_uut_tstcases\\sergio_instrument.yaml@sim"
        )

    def test_get_resource(self, scope_obj):
        assert scope_obj.get_resource() == True

    @pytest.mark.parametrize("expected_freq", [
        ({'freq_limits': [995, 1005]})
    ])
    def test_meas_freq(self, expected_freq, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_freq()
        min_limit = expected_freq.get('freq_limits')[0]
        max_limit = expected_freq.get('freq_limits')[1]
        assert res > min_limit
        assert res < max_limit

    @pytest.mark.parametrize("expected", [
        ({'limits': [0.00095, 0.00105]})
    ])
    def test_meas_period(self, expected, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_period()
        min_limit = expected.get('limits')[0]
        max_limit = expected.get('limits')[1]
        assert res > min_limit
        assert res < max_limit

    @pytest.mark.parametrize("expected", [
        ({'limits': [4.9, 5.1]})
    ])
    def test_meas_vpp(self, expected, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_vpp()
        min_limit = expected.get('limits')[0]
        max_limit = expected.get('limits')[1]
        assert res > min_limit
        assert res < max_limit

    @pytest.mark.parametrize("expected", [
        ({'limits': [2.4, 2.6]})
    ])
    def test_meas_vavg(self, expected, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_vavg()
        min_limit = expected.get('limits')[0]
        max_limit = expected.get('limits')[1]
        assert res > min_limit
        assert res < max_limit

    @pytest.mark.parametrize("expected", [
        ({'limits': [0.0, 0.1]})
    ])
    def test_meas_vmin(self, expected, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_vmin()
        min_limit = expected.get('limits')[0]
        max_limit = expected.get('limits')[1]
        assert res > min_limit
        assert res < max_limit

    @pytest.mark.parametrize("expected", [
        ({'limits': [5.0, 6.0]})
    ])
    def test_meas_vmax(self, expected, scope_obj):
        scope_obj.get_resource()
        res = scope_obj.meas_vmax()
        min_limit = expected.get('limits')[0]
        max_limit = expected.get('limits')[1]
        assert res > min_limit
        assert res < max_limit


pytest.main(['-v'])
