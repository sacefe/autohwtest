import logging
import coloredlogs
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtWidgets, QtGui
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
            table.setStyleSheet("background-color: rgb(25, 25, 25); color: rgb(157, 168, 168)")
            table.setColumnCount(len(table_data[0]))
            table.setHorizontalHeaderLabels(column_names)
            table.setRowCount(len(table_data))

            header = table.horizontalHeader()

            header.setStyleSheet("background-color: rgb(25, 25, 25); color: rgb(157, 168, 168)")
            for row, row_data in enumerate(table_data):
                for col, col_name in enumerate(column_names):
                    # if row_data[col_name] == "FAIL":
                    #     table.setStyleSheet("color: rgb(251, 119, 119)")
                    #     table.setC
                    # else:
                    #     table.setStyleSheet("color: rgb(157, 168, 168)")
                    item = QTableWidgetItem(str(row_data[col_name]))
                    table.setItem(row, col, item)
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            table.resizeColumnsToContents()
            header.setStretchLastSection(True)
            # delegate P/F font attributes
            delegate = StyledItemDelegate(table)
            table.setItemDelegate(delegate)

        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <load_testplan>: {e}")


class StyledItemDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        # print(index.data())
        if index.data() == "FAIL":
            option.font.setItalic(True)
            option.palette.setBrush(QtGui.QPalette.Text, QtGui.QColor(251, 119, 119))
        elif index.data() == "PASS":
            option.font.setItalic(True)
            option.palette.setBrush(QtGui.QPalette.Text, QtGui.QColor(115, 210, 22))

