from PyQt5.QtWidgets import *
from acaPanelLogged_python import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal


class AcaLoggedPage(QMainWindow):
    name_surname_signal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.stuLoggedForm = Ui_MainWindow()
        self.stuLoggedForm.setupUi(self)

        self.name_surname_signal.connect(self.setHelloSignal)

    def setHelloSignal(self, name, surname):
        self.stuLoggedForm.label.setText("Hoşgeldiniz " + name + " " + surname)