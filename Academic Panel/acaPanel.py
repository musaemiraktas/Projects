from PyQt5.QtWidgets import *
from acaPanel_python import Ui_Form
from acaPanelLogged import AcaLoggedPage
from database import connect_to_database, query_database
import random
import string

class AcaLoginPage(QWidget):
    conn = connect_to_database("postgres", "admin1234", "localhost", "5432", "yazlab1")

    cur = conn.cursor()

    """
    cur.execute("SELECT * FROM academic_names")
    teachers = cur.fetchall()
    interests = [1, 2, 3, 4]
                        #öğretmenlere ilgi alanı atamak için
    for teacher in teachers:
        random_interest = random.choice(interests)

        cur.execute("INSERT INTO academic_interest (id, interest) VALUES (%s, %s)",
                    (teacher[0], random_interest))

"""

    def __init__(self):
        super().__init__()
        self.acaLoginForm = Ui_Form()
        self.acaLoginForm.setupUi(self)

        self.acaLoginForm.pushButton_login.clicked.connect(self.Login)

        self.acaLoggedForm = AcaLoggedPage()




    def Login(self):
        username = self.acaLoginForm.lineEdit_username.text()
        password = self.acaLoginForm.lineEdit_password.text()
        parameters = (username, password)

        query = "SELECT id FROM academics WHERE username = %s AND password = %s"
        query_name = "SELECT name, surname FROM academic_names WHERE id = %s"

        try:
            user_id = query_database(self.conn, query, parameters)  # İlgili kullanıcının ID'si
            user_name_surname = query_database(self.conn, query_name, user_id)
            print(user_name_surname)
            # user_name = user_name_surname[0][0]
            # user_surname = user_name_surname[0][1]
            print(user_id)

            if user_id:
                if user_name_surname:
                    user_name = user_name_surname[0][0]
                    user_surname = user_name_surname[0][1]
                    self.acaLoggedForm.name_surname_signal.emit(user_name, user_surname)
                    self.acaLoggedForm.show()
                    self.hide()
                else:
                    self.acaLoginForm.label_loginInfo.setText("Kullanıcı adı bulunamadı!")
            else:
                self.acaLoginForm.label_loginInfo.setText("Giriş bilgileri eksik ya da hatalı!")

        except Exception as e:
            print(f"Hata: {e}")
            self.acaLoginForm.label_loginInfo.setText("Giriş bilgileri eksik ya da hatalı!")

