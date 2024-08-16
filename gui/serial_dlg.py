from PySide6.QtWidgets import (
    QLabel, QDialog, QDialogButtonBox, QLineEdit,
    QVBoxLayout, QSpacerItem, QSizePolicy
)


class SerialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("SERIAL NUMBER")
        self.setStyleSheet(
            "background-color: rgb(22, 22, 22);"
            "color: rgb(186, 189, 182)"
            # "border: 3px solid rgb(45, 45, 45);"
        )
        qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.setStyleSheet(
            "background-color: rgb(25, 25, 25);"
            "color: rgb(186, 189, 182)"
        )
        self.layout = QVBoxLayout()
        self.layout.setSpacing(2)
        vertical_spacer = QSpacerItem(10, 10,
                                      QSizePolicy.Policy.Minimum,
                                      QSizePolicy.Policy.Fixed)
        message = QLabel("Enter product information")
        message.setStyleSheet("border: None;")
        self.layout.addWidget(message)
        self.layout.addSpacerItem(vertical_spacer)
        lbl_serial = QLabel("Serial number:")
        lbl_serial.setStyleSheet("border: None;")
        self.serial = QLineEdit()
        self.serial.setStyleSheet("background-color: rgb(211, 215, 207); "
                                  "color: rgb(25, 25, 25)")
        self.layout.addWidget(lbl_serial)
        self.layout.addWidget(self.serial)
        lbl_empty = QLabel("")
        self.layout.addWidget(lbl_empty)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
