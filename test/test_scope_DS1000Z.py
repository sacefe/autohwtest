from __init__ import *
import pytest
from scope_DS1000Z_sim import Scope_DS1000Z

class Test_Scope_DS1000Z():
    
    @pytest.fixture
    def scopeObj(self):
        return Scope_DS1000Z( 
                IP='172.168.1.139', 
                prefix='DS1Z',  
        )
        
    def test_get_resource(self, scopeObj):
        assert scopeObj.get_resource() == True   
    
    @pytest.mark.parametrize("expected_freq",[
        ({'freq_limits':[995,1005]} )
    ])  
    def test_meas_freq(self, expected_freq, scopeObj):
        scopeObj.get_resource()
        res= scopeObj.meas_freq() 
        minLimit= expected_freq.get('freq_limits')[0]
        maxLimit= expected_freq.get('freq_limits')[1]
        assert res > minLimit
        assert res < maxLimit
        