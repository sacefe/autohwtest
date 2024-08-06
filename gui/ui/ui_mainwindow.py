# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QColumnView, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import rc_resources
from typing import Optional
import os
STATICS_DIR = (os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "statics"))
ICONS_DIR = (os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "statics",
    "icons"))


class Ui_MainWindow(object):
    def __init__(self,
                 statics_dir: Optional[str] = STATICS_DIR,
                 icons_dir: Optional[str] = ICONS_DIR
                 ):
        self.statics_dir = statics_dir
        self.icons_dir = icons_dir
        # ICONS Dynamic location
        self.icons8_menu = os.path.join(self.icons_dir, "icons8_menu.svg")
        self.icons8_account_1 = os.path.join(self.icons_dir, "icons8_account_1.svg")
        self.icons8_maintenance_2 = os.path.join(self.icons_dir, "icons8_maintenance_2.svg")
        self.icons8_alarm = os.path.join(self.icons_dir, "icons8_alarm.svg")
        self.icons8_minus = os.path.join(self.icons_dir, "icons8_minus.svg")
        self.icons8_collapse_arrow_up = os.path.join(self.icons_dir, "icons8_collapse_arrow_up.svg")
        self.icons8_multiply = os.path.join(self.icons_dir, "icons8_multiply.svg")
        self.icons8_keypad = os.path.join(self.icons_dir, "icons8_keypad.svg")
        self.icons8_todo_list = os.path.join(self.icons_dir, "icons8_todo_list.svg")
        self.icons8_logout_rounded_down = os.path.join(self.icons_dir, "icons8_logout_rounded_down.svg")
        self.icons8_play_48 = os.path.join(self.icons_dir, "icons8_play_48.png")
        self.icons8_stop_circled_48 = os.path.join(self.icons_dir, "icons8_stop_circled_48.png")
        self.icons8_pause_button_48 = os.path.join(self.icons_dir, "icons8_pause_button_48.png")
        self.icons8_step_into_48 = os.path.join(self.icons_dir, "icons8_step_into_48.png")
        self.icons8_step_over_48 = os.path.join(self.icons_dir, "icons8_step_over_48.png")
        self.icons8_step_out_48 = os.path.join(self.icons_dir, "icons8_step_out_48.png")

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 627)
        self.actionsign_in = QAction(MainWindow)
        self.actionsign_in.setObjectName(u"actionsign_in")
        self.actionsign_out = QAction(MainWindow)
        self.actionsign_out.setObjectName(u"actionsign_out")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBar = QFrame(self.centralwidget)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 30))
        self.toolBar.setMaximumSize(QSize(16777215, 30))
        self.toolBar.setFrameShape(QFrame.Shape.NoFrame)
        self.toolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.toolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ToogleButton = QFrame(self.toolBar)
        self.ToogleButton.setObjectName(u"ToogleButton")
        self.ToogleButton.setMinimumSize(QSize(30, 30))
        self.ToogleButton.setMaximumSize(QSize(30, 30))
        self.ToogleButton.setStyleSheet(u"background-color: rgb(59, 65, 71);")
        self.ToogleButton.setFrameShape(QFrame.Shape.NoFrame)
        self.ToogleButton.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ToogleButton)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btnHamburger = QPushButton(self.ToogleButton)
        self.btnHamburger.setObjectName(u"btnHamburger")
        self.btnHamburger.setMinimumSize(QSize(30, 30))
        self.btnHamburger.setMaximumSize(QSize(30, 30))
        self.btnHamburger.setSizeIncrement(QSize(0, 0))
        self.btnHamburger.setBaseSize(QSize(0, 0))
        self.btnHamburger.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-left: 3px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon = QIcon()
        icon.addFile(self.icons8_menu, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHamburger.setIcon(icon)
        self.btnHamburger.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.btnHamburger)


        self.horizontalLayout.addWidget(self.ToogleButton)

        self.headerFrame = QFrame(self.toolBar)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.headerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_1 = QSpacerItem(10, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_1)

        self.lblTestSeq = QLabel(self.headerFrame)
        self.lblTestSeq.setObjectName(u"lblTestSeq")
        self.lblTestSeq.setStyleSheet(u"color: rgb(176, 176, 176);")

        self.horizontalLayout_2.addWidget(self.lblTestSeq)

        self.horizontalSpacer_2 = QSpacerItem(100, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.UserFrame = QFrame(self.headerFrame)
        self.UserFrame.setObjectName(u"UserFrame")
        self.UserFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.UserFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.UserFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 20, 0)
        self.btnLogin = QPushButton(self.UserFrame)
        self.btnLogin.setObjectName(u"btnLogin")
        icon1 = QIcon()
        icon1.addFile(self.icons8_account_1, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLogin.setIcon(icon1)
        self.btnLogin.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btnLogin)

        self.btnToolbox = QPushButton(self.UserFrame)
        self.btnToolbox.setObjectName(u"btnToolbox")
        icon2 = QIcon()
        icon2.addFile(self.icons8_maintenance_2, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnToolbox.setIcon(icon2)
        self.btnToolbox.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btnToolbox)

        self.btnAlarm = QPushButton(self.UserFrame)
        self.btnAlarm.setObjectName(u"btnAlarm")
        self.btnAlarm.setMinimumSize(QSize(30, 30))
        self.btnAlarm.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(self.icons8_alarm, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAlarm.setIcon(icon3)
        self.btnAlarm.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btnAlarm)


        self.horizontalLayout_2.addWidget(self.UserFrame)


        self.horizontalLayout.addWidget(self.headerFrame)

        self.ActionFrame = QFrame(self.toolBar)
        self.ActionFrame.setObjectName(u"ActionFrame")
        self.ActionFrame.setMinimumSize(QSize(100, 30))
        self.ActionFrame.setStyleSheet(u"background-color: rgb(22, 22, 22);")
        self.ActionFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ActionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.ActionFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnMin = QPushButton(self.ActionFrame)
        self.btnMin.setObjectName(u"btnMin")
        self.btnMin.setMinimumSize(QSize(30, 30))
        self.btnMin.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(self.icons8_minus, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMin.setIcon(icon4)
        self.btnMin.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.btnMin)

        self.btnMax = QPushButton(self.ActionFrame)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMinimumSize(QSize(30, 20))
        self.btnMax.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(self.icons8_collapse_arrow_up, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMax.setIcon(icon5)
        self.btnMax.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.btnMax)

        self.btnClose = QPushButton(self.ActionFrame)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(40, 30))
        self.btnClose.setMaximumSize(QSize(40, 30))
        icon6 = QIcon()
        icon6.addFile(self.icons8_multiply, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon6)
        self.btnClose.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.btnClose)


        self.horizontalLayout.addWidget(self.ActionFrame)


        self.verticalLayout.addWidget(self.toolBar)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setFrameShape(QFrame.Shape.NoFrame)
        self.Body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Body)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.sideNav = QFrame(self.Body)
        self.sideNav.setObjectName(u"sideNav")
        self.sideNav.setMinimumSize(QSize(43, 0))
        self.sideNav.setMaximumSize(QSize(200, 16777215))
        self.sideNav.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.sideNav.setFrameShape(QFrame.Shape.NoFrame)
        self.sideNav.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sideNav)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_A = QFrame(self.sideNav)
        self.frame_A.setObjectName(u"frame_A")
        self.frame_A.setMinimumSize(QSize(200, 150))
        self.frame_A.setMaximumSize(QSize(200, 170))
        self.frame_A.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_A.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_A)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(19, 7, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.lblStation = QLabel(self.frame_A)
        self.lblStation.setObjectName(u"lblStation")
        self.lblStation.setStyleSheet(u"color: rgb(154, 154, 149);\n"
"font: 700 italic 12pt \"Ubuntu\";")
        self.lblStation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblStation)

        self.verticalSpacer_2 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btnDashboard = QPushButton(self.frame_A)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setMinimumSize(QSize(200, 45))
        self.btnDashboard.setMaximumSize(QSize(200, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.btnDashboard.setFont(font)
        self.btnDashboard.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(self.icons8_keypad, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDashboard.setIcon(icon7)
        self.btnDashboard.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btnDashboard)

        self.btnTestExecute = QPushButton(self.frame_A)
        self.btnTestExecute.setObjectName(u"btnTestExecute")
        self.btnTestExecute.setMinimumSize(QSize(200, 45))
        self.btnTestExecute.setMaximumSize(QSize(200, 45))
        self.btnTestExecute.setFont(font)
        self.btnTestExecute.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(self.icons8_todo_list, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTestExecute.setIcon(icon8)
        self.btnTestExecute.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.btnTestExecute)

        self.comboBoxProducts = QComboBox(self.frame_A)
        self.comboBoxProducts.setObjectName(u"comboBoxProducts")
        self.comboBoxProducts.setStyleSheet(u"color: rgb(154, 154, 149);")

        self.verticalLayout_2.addWidget(self.comboBoxProducts)

        self.verticalSpacer = QSpacerItem(20, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_7.addWidget(self.frame_A)

        self.frame_B = QFrame(self.sideNav)
        self.frame_B.setObjectName(u"frame_B")
        self.frame_B.setMinimumSize(QSize(0, 0))
        self.frame_B.setMaximumSize(QSize(200, 80))
        self.frame_B.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_B.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_B)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.treeSequence = QTreeWidget(self.frame_B)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeSequence.setHeaderItem(__qtreewidgetitem)
        self.treeSequence.setObjectName(u"treeSequence")
        self.treeSequence.setHeaderHidden(False)
        self.treeSequence.setColumnCount(1)

        self.verticalLayout_3.addWidget(self.treeSequence)


        self.verticalLayout_7.addWidget(self.frame_B)

        self.frame_C = QFrame(self.sideNav)
        self.frame_C.setObjectName(u"frame_C")
        self.frame_C.setMinimumSize(QSize(200, 285))
        self.frame_C.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_C.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_C)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.treeExecuted = QTreeWidget(self.frame_C)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeExecuted.setHeaderItem(__qtreewidgetitem1)
        self.treeExecuted.setObjectName(u"treeExecuted")

        self.verticalLayout_4.addWidget(self.treeExecuted)


        self.verticalLayout_7.addWidget(self.frame_C)

        self.frame_D = QFrame(self.sideNav)
        self.frame_D.setObjectName(u"frame_D")
        self.frame_D.setMinimumSize(QSize(200, 50))
        self.frame_D.setMaximumSize(QSize(200, 50))
        self.frame_D.setStyleSheet(u"")
        self.frame_D.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_D.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_D)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnSignout = QPushButton(self.frame_D)
        self.btnSignout.setObjectName(u"btnSignout")
        self.btnSignout.setMinimumSize(QSize(200, 45))
        self.btnSignout.setMaximumSize(QSize(200, 45))
        self.btnSignout.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(204, 204, 204);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(self.icons8_logout_rounded_down, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSignout.setIcon(icon9)
        self.btnSignout.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btnSignout)


        self.verticalLayout_7.addWidget(self.frame_D)


        self.horizontalLayout_3.addWidget(self.sideNav)

        self.Container = QFrame(self.Body)
        self.Container.setObjectName(u"Container")
        self.Container.setStyleSheet(u"background-color: rgb(125,1 25,125);")
        self.Container.setFrameShape(QFrame.Shape.NoFrame)
        self.Container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Container)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.Container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.page_TestExecute = QWidget()
        self.page_TestExecute.setObjectName(u"page_TestExecute")
        self.page_TestExecute.setMinimumSize(QSize(0, 0))
        self.page_TestExecute.setStyleSheet(u"background-color: rgb(22, 22, 22);")
        self.verticalLayout_11 = QVBoxLayout(self.page_TestExecute)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.page_TestExecute)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 0, 2, 0)
        self.tabStepSequence_3 = QTabWidget(self.frame_4)
        self.tabStepSequence_3.setObjectName(u"tabStepSequence_3")
        self.tabStepSequence_3.setMinimumSize(QSize(635, 376))
        self.tabStepSequence_3.setStyleSheet(u"color: rgb(154, 154, 149);")
        self.tabStepSequence_3.setTabsClosable(False)
        self.tabStepSequence_3.setMovable(False)
        self.tabStepSequence_3.setTabBarAutoHide(False)
        self.sequence = QWidget()
        self.sequence.setObjectName(u"sequence")
        palette = QPalette()
        brush = QBrush(QColor(154, 154, 149, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(22, 22, 22, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(154, 154, 149, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.sequence.setPalette(palette)
        self.sequence.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255)\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QTabWidget:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QTabWidget:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.sequence)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.sequence)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(634, 350))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableSequence = QTableWidget(self.frame_5)
        if (self.tableSequence.columnCount() < 3):
            self.tableSequence.setColumnCount(3)
        if (self.tableSequence.rowCount() < 10):
            self.tableSequence.setRowCount(10)
        self.tableSequence.setObjectName(u"tableSequence")
        self.tableSequence.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableSequence.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.tableSequence.setRowCount(10)
        self.tableSequence.setColumnCount(3)
        self.tableSequence.horizontalHeader().setDefaultSectionSize(57)
        self.tableSequence.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableSequence.horizontalHeader().setStretchLastSection(True)
        self.tableSequence.verticalHeader().setVisible(True)
        self.tableSequence.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_9.addWidget(self.tableSequence)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.sequence)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(632, 180))
        self.frame_6.setMaximumSize(QSize(16777215, 300))
        self.frame_6.setStyleSheet(u"color: rgb(154, 154, 149);")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.tabStepSettings_2 = QTabWidget(self.frame_6)
        self.tabStepSettings_2.setObjectName(u"tabStepSettings_2")
        self.tabStepSettings_2.setMinimumSize(QSize(635, 176))
        self.setup = QWidget()
        self.setup.setObjectName(u"setup")
        self.tabStepSettings_2.addTab(self.setup, "")
        self.specs = QWidget()
        self.specs.setObjectName(u"specs")
        self.specs.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(255, 255, 255)\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QTabWidget:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QTabWidget:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.tabStepSettings_2.addTab(self.specs, "")

        self.horizontalLayout_10.addWidget(self.tabStepSettings_2)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.tabStepSequence_3.addTab(self.sequence, "")
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.verticalLayout_13 = QVBoxLayout(self.test)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.test)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 29))
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"background-color: rgb(25, 25, 25)")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.TestActionFrame = QFrame(self.frame_2)
        self.TestActionFrame.setObjectName(u"TestActionFrame")
        self.TestActionFrame.setMinimumSize(QSize(0, 0))
        self.TestActionFrame.setMaximumSize(QSize(270, 16777215))
        self.TestActionFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.TestActionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.TestActionFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnRun = QPushButton(self.TestActionFrame)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setMinimumSize(QSize(0, 20))
        self.btnRun.setMaximumSize(QSize(45, 20))
        self.btnRun.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(self.icons8_play_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRun.setIcon(icon10)
        self.btnRun.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnRun)

        self.btnStop = QPushButton(self.TestActionFrame)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(0, 20))
        self.btnStop.setMaximumSize(QSize(45, 20))
        self.btnStop.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(self.icons8_stop_circled_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStop.setIcon(icon11)
        self.btnStop.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnStop)

        self.btnPause = QPushButton(self.TestActionFrame)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setMinimumSize(QSize(0, 20))
        self.btnPause.setMaximumSize(QSize(45, 20))
        self.btnPause.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(self.icons8_pause_button_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPause.setIcon(icon12)
        self.btnPause.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnPause)

        self.btnStepInto = QPushButton(self.TestActionFrame)
        self.btnStepInto.setObjectName(u"btnStepInto")
        self.btnStepInto.setMinimumSize(QSize(0, 20))
        self.btnStepInto.setMaximumSize(QSize(45, 20))
        self.btnStepInto.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(self.icons8_step_into_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepInto.setIcon(icon13)
        self.btnStepInto.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnStepInto)

        self.btnStepOver = QPushButton(self.TestActionFrame)
        self.btnStepOver.setObjectName(u"btnStepOver")
        self.btnStepOver.setMinimumSize(QSize(0, 20))
        self.btnStepOver.setMaximumSize(QSize(45, 20))
        self.btnStepOver.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(self.icons8_step_over_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepOver.setIcon(icon14)
        self.btnStepOver.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnStepOver)

        self.btnStepOut = QPushButton(self.TestActionFrame)
        self.btnStepOut.setObjectName(u"btnStepOut")
        self.btnStepOut.setMinimumSize(QSize(0, 20))
        self.btnStepOut.setMaximumSize(QSize(45, 20))
        self.btnStepOut.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(self.icons8_step_out_48, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStepOut.setIcon(icon15)
        self.btnStepOut.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btnStepOut)


        self.verticalLayout_10.addWidget(self.TestActionFrame)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.test)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(636, 345))
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tableTest = QTableWidget(self.frame_7)
        if (self.tableTest.columnCount() < 4):
            self.tableTest.setColumnCount(4)
        if (self.tableTest.rowCount() < 11):
            self.tableTest.setRowCount(11)
        self.tableTest.setObjectName(u"tableTest")
        self.tableTest.setRowCount(11)
        self.tableTest.setColumnCount(4)
        self.tableTest.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTest.horizontalHeader().setDefaultSectionSize(150)
        self.tableTest.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableTest.horizontalHeader().setStretchLastSection(True)
        self.tableTest.verticalHeader().setVisible(True)
        self.tableTest.verticalHeader().setCascadingSectionResizes(False)
        self.tableTest.verticalHeader().setDefaultSectionSize(30)
        self.tableTest.verticalHeader().setProperty("showSortIndicator", False)
        self.tableTest.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_11.addWidget(self.tableTest)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.test)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(633, 135))
        self.frame_8.setMaximumSize(QSize(16777215, 300))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.messages = QScrollArea(self.frame_8)
        self.messages.setObjectName(u"messages")
        self.messages.setStyleSheet(u"")
        self.messages.setFrameShadow(QFrame.Shadow.Sunken)
        self.messages.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 634, 156))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.columnView = QColumnView(self.scrollAreaWidgetContents)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setStyleSheet(u"selection-background-color: rgb(140, 140, 140);")

        self.verticalLayout_14.addWidget(self.columnView)

        self.messages.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.messages)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.tabStepSequence_3.addTab(self.test, "")
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.tabStepSequence_3.addTab(self.results, "")

        self.verticalLayout_9.addWidget(self.tabStepSequence_3)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_TestExecute)
        self.page_DashBoard = QWidget()
        self.page_DashBoard.setObjectName(u"page_DashBoard")
        self.frame_3 = QFrame(self.page_DashBoard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(170, 240, 291, 37))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lblDashboard_TBD = QLabel(self.frame_3)
        self.lblDashboard_TBD.setObjectName(u"lblDashboard_TBD")
        self.lblDashboard_TBD.setMinimumSize(QSize(34, 18))
        self.lblDashboard_TBD.setStyleSheet(u"color: rgb(52, 101, 164);\n"
"font: 700 italic 20pt \"Ubuntu Mono\";")

        self.verticalLayout_15.addWidget(self.lblDashboard_TBD)

        self.stackedWidget.addWidget(self.page_DashBoard)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.Container)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabStepSequence_3.setCurrentIndex(1)
        self.tabStepSettings_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsign_in.setText(QCoreApplication.translate("MainWindow", u"sign in", None))
        self.actionsign_out.setText(QCoreApplication.translate("MainWindow", u"sign out", None))
        self.btnHamburger.setText("")
        self.lblTestSeq.setText(QCoreApplication.translate("MainWindow", u"Test Sequence", None))
        self.btnLogin.setText("")
        self.btnToolbox.setText("")
        self.btnAlarm.setText("")
        self.btnMin.setText("")
        self.btnMax.setText("")
        self.btnClose.setText("")
        self.lblStation.setText(QCoreApplication.translate("MainWindow", u"lblStation", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.btnTestExecute.setText(QCoreApplication.translate("MainWindow", u"Test Execute", None))
        self.btnSignout.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
        self.tabStepSettings_2.setTabText(self.tabStepSettings_2.indexOf(self.setup), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.tabStepSettings_2.setTabText(self.tabStepSettings_2.indexOf(self.specs), QCoreApplication.translate("MainWindow", u"Specs", None))
        self.tabStepSequence_3.setTabText(self.tabStepSequence_3.indexOf(self.sequence), QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.btnRun.setText("")
        self.btnStop.setText("")
        self.btnPause.setText("")
        self.btnStepInto.setText("")
        self.btnStepOver.setText("")
        self.btnStepOut.setText("")
        self.tabStepSequence_3.setTabText(self.tabStepSequence_3.indexOf(self.test), QCoreApplication.translate("MainWindow", u"Test", None))
        self.tabStepSequence_3.setTabText(self.tabStepSequence_3.indexOf(self.results), QCoreApplication.translate("MainWindow", u"Results", None))
        self.lblDashboard_TBD.setText(QCoreApplication.translate("MainWindow", u"Under Construction", None))
    # retranslateUi

