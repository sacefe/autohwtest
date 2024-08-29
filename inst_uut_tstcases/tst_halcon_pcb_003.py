import os
import configparser
from inst_uut_tstcases.scope_DS1000Z_sim import ScopeDS1000zSim
from inst_uut_tstcases.lidar import Lidar


# local initialization data
BASEDIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
initFile = BASEDIR + '/config.ini'
config.read(initFile)
SIM = True  # False
args = (config.get('APP', 'VERSION'), SIM)


class HalconPcbPn003:
    def __init__(self):
        self.scope = ScopeDS1000zSim(
            ip='172.168.1.139',
            prefix='DS1Z',
        )
        self.lidar = Lidar(
            args,
            REGTEMPCPU=config.get("REG", "REGTEMPCPU"),
            # kwargs with default values
            HOST=config.get("APP", "HOST"),
            PORT=config.getint("APP", "PORT"),
            RETRY_ATTEMPTS=config.getint("APP", "RETRY_ATTEMPTS"),
            SOCKET_TIMEOUT=config.getint("APP", "SOCKET_TIMEOUT"),
        )

    def read_product_sn(self):
        conn = self.lidar.connect_lidar()
        sn = -1
        if conn:
          sn = self.lidar.get_sn()
        return sn

    def get_lidar_rpm_period(self) -> float:
        conn = self.lidar.connect_lidar()
        calc_time = -1
        if conn:
            lidar_rpm = self.lidar.read_rpm()
            calc_freq = lidar_rpm/60
            calc_time = 1/calc_freq
        return round(calc_time, 5)

    def get_scope_rpm_period(self) -> float:
        res = self.scope.get_resource()
        period_rpm = -1
        if res:
            period_rpm = self.scope.meas_period()
        return round(period_rpm, 5)

    def compare_rpm_period(self) -> bool:
        res = self.scope.get_resource()
        conn = self.lidar.connect_lidar()
        result: bool = False
        if res and conn:
            lidar_rpm_period, scope_rpm_period = -1, 1
            lidar_rpm_period = self.get_lidar_rpm_period()
            scope_rpm_period = self.get_scope_rpm_period()
            result = lidar_rpm_period == scope_rpm_period
        return result


obj = HalconPcbPn003()
print(obj.read_product_sn())
print(obj.get_lidar_rpm_period())
print(obj.get_scope_rpm_period())
print(obj.compare_rpm_period())



