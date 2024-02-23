from PyQt5.QtWidgets import *
from anaPanel_python import Ui_Form
from stuPanel import StuLoginPage
from acaPanel import AcaLoginPage
from managerPanel import ManagerLoginPage
from stuPanelLogged import StuLoggedPage

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.mainForm.pushButton_ogrenciGiris.clicked.connect(self.stuLogin)
        self.mainForm.pushButton_akademikGiris.clicked.connect(self.acaLogin)
        self.mainForm.pushButton_yoneticiGiris.clicked.connect(self.managerLogin)

        self.openStuLogin = StuLoginPage()
        self.openAcaLogin = AcaLoginPage()
        self.openManagerLogin = ManagerLoginPage()

        self.openStuLogged = StuLoggedPage()

    def stuLogin(self):
        self.hide()
        self.openStuLogin.show()

    def acaLogin(self):
        self.hide()
        self.openAcaLogin.show()
    def managerLogin(self):
        self.hide()
        self.openManagerLogin.show()


