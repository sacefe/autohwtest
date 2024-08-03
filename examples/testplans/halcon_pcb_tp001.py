import os
from pathlib import Path
from time import sleep
from seq.tst_sequence import TestSequence, Test, ArchiveManager
from random import choice, random
# from threading import Thread, Semaphore
from inst_uut_tstcases.scope_DS1000Z_sim import ScopeDS1000zSim
from inst_uut_tstcases.lidar import Lidar
import configparser
import sys


# EXAMPLES START ##############
# class TestProd1(Test):
#     """
#     test example P/F
#     """
#
#     def __init__(self):
#         super().__init__(
#             nickname="test_1",
#             pass_if=True)
#         return
#
#     # make setting as need before execute test
#     def setup(self, is_passing):
#         sleep(0.1)
#         return True
#
#     # overriding the execute method
#     def execute(self, is_passing):
#         return choice([True] * 3 + [False])
#
#     def teardown(self, is_passing):
#         # again, simulating another long-running process...
#         sleep(0.1)
#
#
# class TestProd2(Test):
#     """
#     test example min/max value
#     """
#
#     def __init__(self):
#         super().__init__(
#             nickname="test_2",
#             min_value=7.2,
#             max_value=7.8)
#         return
#
#     # make setting as need before execute test
#     def setup(self, is_passing):
#         sleep(0.1)
#         return True
#
#     # overriding the execute method
#     def execute(self, is_passing):
#         result = 7.5 + random()
#         return result
#
#     def teardown(self, is_passing):
#         # again, simulating another long-running process...
#         sleep(0.1)
# EXAMPLES END ################


class ScopeDS1000zInstrument(ScopeDS1000zSim):
    def __init__(self):
        scope = super().__init__(
            ip='172.168.1.139',
            prefix='DS1Z',
        )


class ScopeDS1000sGetResource(Test):
    """
    test example min/max value
    """
    def __init__(self):
        super().__init__(
            nickname="ScopeDS1000sGetResource",
            pass_if=True)
        self.scope = ScopeDS1000zInstrument()

    # make setting as need before execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.scope.get_resource()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()
        sleep(0.1)


class ScopeDS1000zMeasFreq(Test):
    """
    test example min/max value
    """
    def __init__(self):
        super().__init__(
            nickname="ScopeDS1000zMeasFreq",
            min_value=995.0,
            max_value=1005.0,
            significant_figures=1
        )
        self.scope = ScopeDS1000zInstrument()

    #  make setting as need before execute test
    def setup(self, is_passing):
        res = self.scope.get_resource()
        return res

    #  overriding the execute method
    def execute(self, is_passing):
        res = self.scope.meas_freq()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()


class ScopeDS1000zMeasPeriod(Test):
    """
    test example min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="ScopeDS1000zMeasPeriod",
            min_value=0.00095,
            max_value=0.00105,
            significant_figures=3
        )
        self.scope = ScopeDS1000zInstrument()

    #  make setting as need before execute test
    def setup(self, is_passing):
        res = self.scope.get_resource()
        return res

    #  overriding the execute method
    def execute(self, is_passing):
        res = self.scope.meas_period()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        if self.scope:
            self.scope.close_resource()


# config initialization data
BASEDIR= os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
initFile = BASEDIR + '/config.ini'
config.read(initFile)
SIM = True  # False
args = (config.get('APP', 'VERSION'), SIM)


class LidarSystem(Lidar):
    def __init__(self):
        super().__init__(args,
                         REGTEMPCPU=config.get("REG", "REGTEMPCPU"),
                         # kwargs with default values
                         HOST=config.get("APP", "HOST"),
                         PORT=config.getint("APP", "PORT"),
                         RETRY_ATTEMPTS=config.getint("APP", "RETRY_ATTEMPTS"),
                         SOCKET_TIMEOUT=config.getint("APP", "SOCKET_TIMEOUT"),
                         )


class LidarConnection(Test):
    """
    test case Pass/Fail
    """

    def __init__(self):
        super().__init__(
            nickname="LidarConnection",
            pass_if=True)
        self.lidar_connection = LidarSystem()

    #  make setting as need before execute test
    def setup(self, is_passing):
        sleep(0.1)
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class LidarTemperature(Test):
    """
    test case min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="LidarTemperature",
            min_value=20,
            max_value=70)
        self.lidar_connection = LidarSystem()

    # make setting as need before execute test
    def setup(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    # overriding the execute method
    def execute(self, is_passing):
        res = self.lidar_connection.get_temperature_cpu()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class LidarGetSN(Test):
    """
    test case min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="LidarGetSN",
            pass_if='371182210154')
        self.lidar_connection = LidarSystem()

    #  make setting as need before execute test
    def setup(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    # overriding the execute method
    def execute(self, is_passing):
        res = self.lidar_connection.get_sn()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class LidarReadPRM(Test):
    """
    test case min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="LidarReadPRM",
            pass_if=5400)
        self.lidar_connection = LidarSystem()

    #  make setting as need before execute test
    def setup(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    # overriding the execute method
    def execute(self, is_passing):
        res = self.lidar_connection.read_rpm()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class LidarReadRegPl(Test):
    """
    test case min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="LidarReadRegPl",
            pass_if=True)
        self.lidar_connection = LidarSystem()

    # make setting as need before execute test
    def setup(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    # overriding the execute method
    def execute(self, is_passing):
        reg = config.get("REG", "REGPOLYDELAY")
        reg_value = self.lidar_connection.read_regpl(reg)
        res = reg_value.startswith('reg_rd: 0x330 0x13')  # 'reg_rd: 0x330 0x13c07\n'
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class LidarWriteRegPl(Test):
    """
    test case min/max value
    """

    def __init__(self):
        super().__init__(
            nickname="LidarWriteRegPl",
            pass_if=True)
        self.lidar_connection = LidarSystem()

    # make setting as need before execute test
    def setup(self, is_passing):
        res = self.lidar_connection.connect_lidar()
        return res

    # overriding the execute method
    def execute(self, is_passing):
        reg = config.get("REG", "REGSARATE")
        self.lidar_connection.write_regpl(reg, '0x200')
        reg_value = self.lidar_connection.read_regpl(reg)
        # res1= reg_value.startswith('reg_rd: 0x328 0x200\n')
        res1 = reg_value.startswith('reg_rd: 0x328')
        # return res
        self.lidar_connection.write_regpl(reg, '0x100')
        reg_value = self.lidar_connection.read_regpl(reg)
        # res2= reg_value.startswith('reg_rd: 0x328 0x100\n')
        res2 = reg_value.startswith('reg_rd: 0x328')
        return res1 and res2

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


# TODO
class TestPlan:
    def __init__(self):
        return

    def execute(self):
        return True


def main():
    sequence = [  # TestProd1(),
        # TestProd2(),
        ScopeDS1000sGetResource(),
        ScopeDS1000zMeasFreq(),
        ScopeDS1000zMeasPeriod(),
        LidarConnection(),
        LidarTemperature(),
        LidarGetSN(),
        LidarReadPRM(),
        LidarReadRegPl(),
        LidarWriteRegPl()
    ]

    # create the archive manager
    # am = ArchiveManager(data_format=1)
    am = ArchiveManager(path='../..')

    # create the test sequence using the
    # sequence and archive manager objects from above
    ts = TestSequence(sequence=sequence,
                      archive_manager=am,
                      auto_run=False)

    for x in range(1):
        ts.start_tests()
        while (ts.get_state != "complete / ready" and
               ts.get_state != "aborted / ready"):
            sleep(1)
        # ts2.start_tests()
        # sleep(0.5)


if __name__ == "__main__":
    main()
