import os
import importlib
from time import sleep
from seq.tst_sequence import TestSequence, Test, ArchiveManager


class Tester:
    def __init__(self):
        self.archive_path = "."
        self.cycles = 1

    def run_all_sequence(self,
                         testplan_name,
                         testplans_dir,
                         testplan):
        sequence = []
        # module = importlib.import_module("examples.testplans.halcon_pcb_tp001")
        mod_path_arr = [testplan_name]
        curr_path = testplans_dir
        while curr_path:
            curr_path, section = os.path.split(curr_path)
            if section:
                mod_path_arr.append(section)
            else:
                mod_path_arr.append(curr_path)
        mod_path_arr.reverse()
        mod_path = ".".join(mod_path_arr)
        # ex "examples.testplans.halcon_pcb_tp001"
        module = importlib.import_module(mod_path)
        for testModule in testplan:
            # ex class ScopeDS1000sGetResource()
            test_case = getattr(module, testModule['TEST_NAME'])
            sequence.append(test_case())

        if not self.archive_path:
            self.archive_path = '.'
        am = ArchiveManager(path=self.archive_path)

        # create the test sequence using the
        # sequence and archive manager objects from above
        ts = TestSequence(sequence=sequence,
                          archive_manager=am,
                          auto_run=False)

        for x in range(self.cycles):
            ts.start_tests()
            while (ts.get_state != "complete / ready" and
                   ts.get_state != "aborted / ready"):
                sleep(1)

        return ts.seq_test_results
