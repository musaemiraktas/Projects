from PyQt5.QtWidgets import *
from managerPanel_python import Ui_Form
from managerPanelLogged import ManagerLoggedPage

class ManagerLoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.managerLoginForm = Ui_Form()
        self.managerLoginForm.setupUi(self)

        self.managerLoggedForm = ManagerLoggedPage()

        self.managerLoginForm.pushButton_login.clicked.connect(self.Login)
    def Login(self):
        username = self.managerLoginForm.lineEdit_username.text()
        password = self.managerLoginForm.lineEdit_password.text()

        if username == "admin" and password == "admin":
            self.managerLoggedForm.show()
            self.hide()
        else:
            self.managerLoginForm.label_loginInfo.setText("Giriş bilgileri eksik ya da hatalı!")