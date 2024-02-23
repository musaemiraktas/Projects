from PyQt5.QtWidgets import *
from stuPanel_python import Ui_Form
from stuPanelLogged import StuLoggedPage
from database import connect_to_database, query_database


class StuLoginPage(QWidget):

    conn = connect_to_database("postgres", "admin1234", "localhost", "5432", "yazlab1")

    def __init__(self):
        super().__init__()
        self.stuLoginForm = Ui_Form()
        self.stuLoginForm.setupUi(self)

        self.stuLoggedForm = StuLoggedPage()

        self.stuLoginForm.pushButton_login.clicked.connect(self.Login)

    def Login(self):
        username = self.stuLoginForm.lineEdit_username.text()
        password = self.stuLoginForm.lineEdit_password.text()
        parameters = (username, password)

        query = "SELECT id FROM students WHERE username = %s AND password = %s"
        query_name = "SELECT isim, soyisim FROM student_names WHERE student_id = %s"

        try:
            user_id = query_database(self.conn, query, parameters)  # İlgili kullanıcının ID'si
            user_name_surname = query_database(self.conn, query_name, user_id)
            print(user_name_surname)
            #user_name = user_name_surname[0][0]
            #user_surname = user_name_surname[0][1]
            print(user_id)

            if user_id:
                if user_name_surname:
                    user_name = user_name_surname[0][0]
                    user_surname = user_name_surname[0][1]
                    self.stuLoggedForm.name_surname_signal.emit(user_name, user_surname)
                    self.stuLoggedForm.show()
                    self.hide()
                else:
                    self.stuLoginForm.label_loginInfo.setText("Kullanıcı adı bulunamadı!")
            else:
                self.stuLoginForm.label_loginInfo.setText("Giriş bilgileri eksik ya da hatalı!")

        except Exception as e:
            print(f"Hata: {e}")
            self.stuLoginForm.label_loginInfo.setText("Giriş bilgileri eksik ya da hatalı!")
