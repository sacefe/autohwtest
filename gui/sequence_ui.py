import os
import logging
import coloredlogs
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ui.ui_mainwindow import Ui_MainWindow
from typing import Optional
from loader_data import LoaderData
from loader_widgets import LoaderWidgets
from tester import Tester
from dashboard import Dashboard
from login import LoginDialog
from utils import PageNames

coloredlogs.install(level="INFO")

STATICS_DIR = (os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "static"))
BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))


class SequenceUI(QMainWindow):

    def __init__(self,
                 testplan_dir,
                 station_fp: Optional[str] = "config/station.csv",
                 part_numbers_fp: Optional[str] = "config/part_numbers.csv",
                 loglevel: Optional[callable] = logging.INFO
                 ):
        super(SequenceUI, self).__init__()
        self.ui = Ui_MainWindow(STATICS_DIR)
        self.ui.setupUi(self)
        # set logger
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(loglevel)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.__pos = self.pos()
        self.setWindowFlags(flags)
        self.__activate_toolbar()
        self.__activate_side_nav()
        self.__activate_tst_seq()
        # app self vars
        self.ld_data = LoaderData(
            station_fp=station_fp,
            part_numbers_fp=part_numbers_fp,
        )
        self.dashboard = Dashboard(self.ui)
        self.page_name = PageNames.testExecute.value
        self.lw = LoaderWidgets()
        self.testplans_dir = testplan_dir
        self.testplan_fp = ""
        self.test_exec_fp = ""
        self.station = {}
        self.testplan_name = ""
        self.testplan = []
        self.test_results = []
        self.part_numbers = []
        self.load_station()
        self.load_part_numbers()
        self.ui.Body.setEnabled(False)

    """
    beginning of UI code section
    """

    def mouseMoveEvent(self, event):
        point = QPoint(event.globalPosition().toPoint() - self.__pos)
        self.move(self.x() + point.x(), self.y() + point.y())
        self.__pos = event.globalPosition().toPoint()

    def mousePressEvent(self, event):
        self.__pos = event.globalPosition().toPoint()

    def __activate_toolbar(self):
        self.ui.btnHamburger.clicked.connect(self.__open_close_nav)
        self.ui.btnClose.clicked.connect(self.__close_main_window)
        self.ui.btnMax.clicked.connect(self.__max_restore_main_window)
        self.ui.btnMin.clicked.connect(self.__min_main_window)
        self.ui.btnMin.clicked.connect(self.__min_main_window)
        self.ui.btnAlarm.clicked.connect(self.__alarm)
        self.ui.btnToolbox.clicked.connect(self.__toolbox)
        self.ui.btnLogin.clicked.connect(self.__login)

    def __activate_side_nav(self):
        self.ui.btnDashboard.clicked.connect(self.__dashboard)
        self.ui.btnTestExecute.clicked.connect(self.__execute_test)

    def __activate_tst_seq(self):
        self.ui.btnRun.clicked.connect(self.__run_sequence)
        self.ui.btnStop.clicked.connect(self.__stop_sequence)
        self.ui.btnPause.clicked.connect(self.__pause_sequence)
        self.ui.btnStepInto.clicked.connect(self.__step_into_sequence)
        self.ui.btnStepOver.clicked.connect(self.__step_over_sequence)
        self.ui.btnStepOut.clicked.connect(self.__step_out_sequence)

    def __open_close_nav(self):
        width = self.ui.sideNav.maximumWidth()
        if width == 200:
            self.ui.sideNav.setMaximumWidth(43)
            self.ui.treeSequence.setVisible(False)
            self.ui.treeExecuted.setVisible(False)
        else:
            self.ui.sideNav.setMaximumWidth(200)
            self.ui.treeSequence.setVisible(True)
            self.ui.treeExecuted.setVisible(True)

    def __close_main_window(self):
        self.close()

    def __max_restore_main_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def __min_main_window(self):
        self.showMinimized()

    # TODO
    def __alarm(self):
        self.__logger.info("alarms TBD")

    # TODO
    def __login(self):
        dlg_login = LoginDialog(self)
        # ui = dlg_login. .Ui_Dialog()
        if dlg_login.exec():
            if dlg_login.user.text().lower() == "test" and \
                    dlg_login.password.text().lower() == "password":
                self.ui.Body.setEnabled(True)
            self.__logger.info(f"Success! user is: {dlg_login.user.text()} "
                               f"password is: {dlg_login.password.text()}")
            self.__logger.info("Success!")
        else:
            self.__logger.info("Cancel!")

    # TODO
    def __toolbox(self):
        self.__logger.info("ToolBox TBD")

    # TODO
    def __dashboard(self):
        self.dashboard.activate_page()
        self.__logger.info("Dashboard TBD")

    def __execute_test(self):
        self.ui.stackedWidget.setCurrentIndex(self.page_name)
        self.__logger.info("Execute Test Page")

    # TODO convert to
    def __run_sequence(self):
        """
        run all test cases but individually to have option to abort
        @return:
        """
        if self.testplan_name != "" and self.testplan != []:
            try:
                tester_obj = Tester(
                    testplan_name=self.testplan_name,
                    testplans_dir=self.testplans_dir,
                    testplan=self.testplan)

                table = self.ui.tableTest
                sequence = tester_obj.get_sequence()
                for i, testcase in enumerate(sequence):
                    # QTimer.singleShot(1000, self.__run_sequence)
                    updated_test_result = tester_obj.run_testcase_sequence([testcase])
                    tr = self.ld_data.update_test_exec(i, self.test_results, updated_test_result)
                    self.test_results = tr
                    self.update_test_exec_table()
                    self.__logger.info(f"Run Sequence results: {self.test_results}")
                    table.selectRow(i)
                    table.viewport().setFocus()
                    table.viewport().update()
            except BaseException as e:
                self.__logger.error(f"an exception occurred during the <__run_sequence>: {e}")

        # # this way run all test cases first and then update table
        # if self.testplan_name != "" and self.testplan != []:
        #     tester_obj = Tester(
        #         testplan_name=self.testplan_name,
        #         testplans_dir=self.testplans_dir,
        #         testplan=self.testplan)
        #     sequence = tester_obj.get_sequence()
        #     updated_test_results = tester_obj.run_testcase_sequence(sequence)
        #
        #     tr = self.ld_data.update_all_test_exec(self.test_results, updated_test_results)
        #     self.test_results = tr
        #     self.update_test_exec_table()
        #     self.__logger.info(f"Run Sequence results: {self.test_results}")

    # TODO
    def __stop_sequence(self):
        self.__logger.info("Stop Sequence TBD")

    # TODO
    def __pause_sequence(self):
        self.__logger.info("Pause Sequence TBD")

    # TODO  load sequence when tesplan is loaded or individually each time (save memory)
    def __step_into_sequence(self):
        """
        run one test case already selected in the table
        @return:
        """
        if self.testplan_name != "" and self.testplan != []:
            try:
                tester_obj = Tester(
                    testplan_name=self.testplan_name,
                    testplans_dir=self.testplans_dir,
                    testplan=self.testplan)

                table = self.ui.tableTest
                row = table.currentRow()
                table.setFocus()
                if row == -1:
                    table.selectRow(0)
                row = table.currentRow()
                testcase = tester_obj.get_testcase(row)
                updated_test_result = tester_obj.run_testcase_sequence(testcase)
                tr = self.ld_data.update_test_exec(row, self.test_results, updated_test_result)
                self.test_results = tr
                self.update_test_exec_table()
                row += 1
                if row >= len(self.testplan):
                    row = 0
                table.selectRow(row)
                self.__logger.info(f"Run Sequence results: {self.test_results}")
            except BaseException as e:
                self.__logger.error(f"an exception occurred during the <__step_into_sequence>: {e}")

    # TODO
    def __step_over_sequence(self):
        self.__logger.info("Step Over Sequence TBD")

    # TODO
    def __step_out_sequence(self):
        self.__logger.info("Step Out Sequence TBD")

    """
    #####################################
    beginning of App code section
    #####################################
    """

    def load_testplan_table(self):
        try:
            table = self.ui.tableSequence
            table.clear()
            self.testplan = []
            self.testplan, column_names = self.ld_data.get_testplan(self.testplan_fp)
            self.lw.table_loader(table, self.testplan, column_names)
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <load_testplan_table>: {e}")

    def load_test_exec_table(self):
        try:
            table = self.ui.tableTest
            table.clear()
            self.test_results, column_names = self.ld_data.get_test_exec(self.test_exec_fp)
            self.lw.table_loader(table, self.test_results, column_names)
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <load_test_exec_table>: {e}")

    def update_test_exec_table(self):
        try:
            table = self.ui.tableTest
            table.clear()
            column_names = list(self.test_results[0].keys())
            self.lw.table_loader(table, self.test_results, column_names)
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <load_test_exec_table>: {e}")

    def load_station(self):
        stations, column_names = self.ld_data.get_station_info()
        self.station = stations[0]
        label = self.ui.lblStation
        label.setText(self.station['NAME'])

    def load_part_numbers(self):
        self.part_numbers, column_names = self.ld_data.get_part_numbers()
        cb_pn = self.ui.comboBoxProducts
        cb_pn.clear()
        cb_pn.addItems(pn[0] for pn in self.part_numbers)
        cb_pn.currentIndexChanged.connect(self.cm_products_index_changed)
        cb_pn.currentTextChanged.connect(self.cm_products_text_changed)
        testplan_fp_abs = self.part_numbers[0][1]
        self.testplan_fp = (os.path.join(
            self.testplans_dir,
            testplan_fp_abs))
        self.testplan_name = os.path.splitext(testplan_fp_abs)[0]
        self.lw.tree_seq_update(self.ui.treeSequence,
                                self.testplan_name)
        self.test_exec_fp = self.testplan_fp  # TODO perhaps a different file for results vs Testplan?
        self.load_testplan_table()
        self.load_test_exec_table()

    def cm_products_index_changed(self, i):
        testplan_fp_abs = self.part_numbers[i][1]
        self.testplan_fp = (os.path.join(
            self.testplans_dir,
            testplan_fp_abs))
        self.testplan_name = os.path.splitext(testplan_fp_abs)[0]
        self.lw.tree_seq_update(self.ui.treeSequence,
                                self.testplan_name)
        self.test_exec_fp = self.testplan_fp  # TODO perhaps a different file for results vs Testplan?
        self.load_testplan_table()
        self.load_test_exec_table()

    def cm_products_text_changed(self, s):
        self.__logger.info(s)

# from examples.testplans.halcon_pcb_tp001 import *
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SequenceUI(
#         testplan_dir="/home/demo/sacode/autohwtest/examples/testplans",
#         station_fp="/home/demo/sacode/autohwtest/examples/config/station.csv",
#         part_numbers_fp="/home/demo/sacode/autohwtest/examples/config/part_numbers.csv",
#     )
#     window.show()
#     sys.exit(app.exec())
