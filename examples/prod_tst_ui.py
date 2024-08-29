import os
from PySide6.QtWidgets import *
from gui.sequence_ui import SequenceUI
from examples.testplans.halcon_pcb_tp001 import *

# init
BASEDIR = os.path.dirname(os.path.abspath(__file__))
config_file = configparser.ConfigParser()
config_file.read(BASEDIR + '/config.ini')
# args = (local.get('APP', 'VERSION'), SIM)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SequenceUI(
        #TODO use **args and/or create local file and create directories
        config_file,
        testplan_dir="testplans",
        station_fp="local/station.csv",
        part_numbers_fp="local/part_numbers.csv",
        test_matrix_fp="local/test_matrix.csv",
    )
    window.show()
    sys.exit(app.exec())
