from ui.ui_mainwindow import Ui_MainWindow
from utils import PageNames

class Dashboard:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.page_name = PageNames.dashboard.value

    def activate_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.page_name)
