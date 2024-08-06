import os
from time import sleep
from seq.tst_sequence import TestSequence, Test, ArchiveManager
from inst_uut_tstcases.tst_halcon_pcb_003 import HalconPcbPn003
import configparser


# config initialization data
BASEDIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
initFile = BASEDIR + '/config.ini'
config.read(initFile)
SIM = True  # False
args = (config.get('APP', 'VERSION'), SIM)


class HalconPcbPn003_ReadProductSN(Test):
    """
    test case string value
    """
    def __init__(self):
        super().__init__(
            nickname="HalconPcbPn003_ReadProductSN",
            pass_if='371182210154')
        self.halconPcbPn003 = HalconPcbPn003()

    #  make setting as need before execute test
    def setup(self, is_passing):
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.halconPcbPn003.read_product_sn()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class HalconPcbPn003_GetLidarRpmPeriod(Test):
    """
    test case string value
    """
    def __init__(self):
        super().__init__(
            nickname="HalconPcbPn003_GetLidarRpmPeriod",
            min_value=0.01099,
            max_value=0.01121,
            significant_figures=4
        )
        self.halconPcbPn003 = HalconPcbPn003()

    #  make setting as need before execute test
    def setup(self, is_passing):
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.halconPcbPn003.get_lidar_rpm_period()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class HalconPcbPn003_GetScopeRpmPeriod(Test):
    """
    test case string value
    """
    def __init__(self):
        super().__init__(
            nickname="HalconPcbPn003_GetScopeRpmPeriod",
            min_value=0.01099,
            max_value=0.01121,
            significant_figures=4
        )
        self.halconPcbPn003 = HalconPcbPn003()

    #  make setting as need before execute test
    def setup(self, is_passing):
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.halconPcbPn003.get_scope_rpm_period()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


class HalconPcbPn003_CompareRpmPeriod(Test):
    """
    test case string value
    """
    def __init__(self):
        super().__init__(
            nickname="HalconPcbPn003_CompareRpmPeriod",
            pass_if=True
        )
        self.halconPcbPn003 = HalconPcbPn003()

    #  make setting as need before execute test
    def setup(self, is_passing):
        return True

    # overriding the execute method
    def execute(self, is_passing):
        res = self.halconPcbPn003.compare_rpm_period()
        return res

    def teardown(self, is_passing):
        # again, simulating another long-running process...
        sleep(0.1)


def main():
    sequence = [
        HalconPcbPn003_ReadProductSN(),
        HalconPcbPn003_GetLidarRpmPeriod(),
        HalconPcbPn003_GetScopeRpmPeriod(),
        HalconPcbPn003_CompareRpmPeriod()
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
            sleep(0.1)


if __name__ == "__main__":
    main()
