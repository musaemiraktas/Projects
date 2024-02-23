from PyQt5.QtWidgets import *
from managerPanelLogged_python import Ui_MainWindow

class ManagerLoggedPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.managerLoggedForm = Ui_MainWindow()
        self.managerLoggedForm.setupUi(self)