from PySide6.QtWidgets import (
    QLabel, QDialog, QDialogButtonBox, QLineEdit,
    QVBoxLayout, QSpacerItem, QSizePolicy
)


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("LOGIN")
        self.setStyleSheet(
            "background-color: rgb(22, 22, 22);"
            "color: rgb(154, 154, 149);"
            # "border: 3px solid rgb(45, 45, 45);"
        )
        qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.setStyleSheet(
            "background-color: rgb(25, 25, 25);"
            "color: rgb(154, 154, 149);"
        )
        self.layout = QVBoxLayout()
        self.layout.setSpacing(2)
        vertical_spacer = QSpacerItem(10, 10,
                                      QSizePolicy.Policy.Minimum,
                                      QSizePolicy.Policy.Fixed)
        message = QLabel("Enter your login information")
        message.setStyleSheet("border: None;")
        self.layout.addWidget(message)
        self.layout.addSpacerItem(vertical_spacer)
        lbl_user = QLabel("User:")
        lbl_user.setStyleSheet("border: None;")
        self.user = QLineEdit()
        self.user.setStyleSheet("background-color: rgb(211, 215, 207); "
                           "color: rgb(25, 25, 25)")
        lbl_password = QLabel("Password:")
        lbl_password.setStyleSheet("border: None;")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("background-color: rgb(211, 215, 207); "
                               "color: rgb(25, 25, 25)")
        self.layout.addWidget(lbl_user)
        self.layout.addWidget(self.user)
        self.layout.addWidget(lbl_password)
        self.layout.addWidget(self.password)
        lbl_empty = QLabel("")
        self.layout.addWidget(lbl_empty)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
