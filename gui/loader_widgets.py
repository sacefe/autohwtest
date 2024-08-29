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

    def tree_seq_update(self, tree_widget: QTreeWidget, tree_data):
        # tree_widget.headerItem().setText(1, tree_data)
        tree_widget.addTopLevelItem(QTreeWidgetItem(0))
        tree_widget.topLevelItem(0).setText(0, tree_data)

    def tree_test_history_update(self, tree_widget: QTreeWidget, tree_data, i):
        # tree_widget.headerItem().setText(1, tree_data)
        tree_widget.addTopLevelItem(QTreeWidgetItem(i))
        tree_widget.topLevelItem(i).setText(0, tree_data)

    def table_loader(self, table: QTableWidget, table_data, column_names):
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

    def combobox_loader(self, cbox: QComboBox, cbox_data, cbox_column_names):
        # define model
        cols = len(cbox_data[0])
        model = QStandardItemModel(0, cols)
        for i in range(cols):
            model.setHorizontalHeaderItem(i, QStandardItem(cbox_column_names[i]))
        for row_line in cbox_data:
            items = []
            for col_value in row_line:
                it = QStandardItem(str(col_value))
                items.append(it)
            model.appendRow(items)
        cbox.setModel(model)
        # define  view
        view = QTableView(
            cbox, selectionBehavior=QAbstractItemView.SelectRows
        )
        # Column wit=dth did not work
        view.verticalHeader().setVisible(False)
        view.setColumnWidth(0, 4)
        view.setColumnWidth(1, 10)
        view.setColumnWidth(2, 10)
        view.resizeColumnsToContents()
        # set scroll bar did not work
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        view.horizontalScrollBar().setVisible(True)
        # set view
        cbox.setModelColumn(1)  # show column one first
        cbox.setView(view)


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

