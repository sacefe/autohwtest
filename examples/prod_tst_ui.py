import os
from PySide6.QtWidgets import *
from gui.sequence_ui import SequenceUI
from examples.testplans.halcon_pcb_tp001 import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SequenceUI(
        testplan_dir="testplans",
        station_fp="config/station.csv",
        part_numbers_fp="config/part_numbers.csv",
    )
    window.show()
    sys.exit(app.exec())
