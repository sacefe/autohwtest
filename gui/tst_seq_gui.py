import sys
from PySide6 import QtWidgets
from PySide6 import QtUiTools
from mainwindow import Ui_MainWindow


# BASE_DIR = Path(__file__).resolve().parent   # Figures out the absolute path
# sys.path.append(f"{BASE_DIR}")
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

ui, _ = QtUiTools.loadUiType("mainwindow.ui")


class MainWindow(QtWidgets.QMainWindow , ui):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
