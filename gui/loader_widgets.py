import logging
import coloredlogs
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from typing import Optional

coloredlogs.install(level="INFO")


class LoaderWidgets:
    def __init__(self,
                 loglevel: Optional[callable] = logging.INFO
                 ):
        # set logger
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(loglevel)
        # set logger

    def table_loader(self, table, table_data, column_names):
        try:
            #    self.testplan, column_names = self.ld.get_testplan()
            #    table = self.ui.tableSequence
            table.setStyleSheet("background-color: rgb(25, 25, 25); color: rgb(157, 168, 168)")
            table.setColumnCount(len(table_data[0]))
            table.setHorizontalHeaderLabels(column_names)
            table.setRowCount(len(table_data))

            header = table.horizontalHeader()
            header.setStretchLastSection(True)
            header.setStyleSheet("background-color: rgb(25, 25, 25); color: rgb(157, 168, 168)")

            for row, row_data in enumerate(table_data):
                for col, col_name in enumerate(column_names):
                    item = QTableWidgetItem(str(row_data[col_name]))
                    table.setItem(row, col, item)
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            # header.setResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            table.resizeColumnsToContents()

        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <load_testplan>: {e}")


