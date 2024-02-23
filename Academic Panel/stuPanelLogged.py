from PyQt5.QtWidgets import *
from stuPanelLogged_python import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
import pytesseract
from PIL import Image
from stuTranscript import StuTranscriptPage
from database import *



class StuLoggedPage(QMainWindow):
    conn = connect_to_database("postgres", "admin1234", "localhost", "5432", "yazlab1")
    name_surname_signal = pyqtSignal(str, str)  # İsim ve soyismi iletmek için sinyal

    def __init__(self):
        super().__init__()
        self.stuLoggedForm = Ui_MainWindow()
        self.stuLoggedForm.setupUi(self)
        self.name_surname_signal.connect(self.setHelloLabel)
        #self.stuLoggedForm.action_uploadTranscript.triggered.connect(self.selectFile)

        self.stuTranscriptForm = StuTranscriptPage()
        self.stuLoggedForm.action_enterTranscript.triggered.connect(self.EnterTranscript)

        self.stuLoggedForm.action_transcriptView.triggered.connect(self.ViewTranscriptTable)
        self.load_teachers()
        self.load_interests()


    def setHelloLabel(self, user_name, user_surname):
        self.stuLoggedForm.label.setText("Hoşgeldiniz " + user_name + " " + user_surname)

    def selectFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "Belge Seç", "", "PDF Dosyaları (*.pdf);;Tüm Dosyalar (*)", options=options)
        filePath = "C:/Users/Emir/Desktop/yazlab1/60463366228_Transkript.pdf"
        if filePath:
            print(filePath)
            self.readPDF(filePath)  #burada sıkıntı yok.

    def readPDF(self, file_path):
        # PDF dosyasını görüntüye dönüştürme ve OCR işlemini gerçekleştirme
        text = self.performOCR(file_path)

        # Ders bilgilerini konsola yazdırma
        print(text)

    def performOCR(self, image_path):
        # PDF dosyasını görüntüye dönüştürme
        image = Image.open(image_path)

        # OCR işlemini gerçekleştirme
        text = pytesseract.image_to_string(image)

        return text

    def EnterTranscript(self):
        try:
            conn = connect_to_database("postgres", "admin1234", "localhost", "5432", "yazlab1")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transcript_info")
            rows = cursor.fetchall()
            data = "\n".join(map(str, rows))  # rows listesini metin haline getir
            self.stuTranscriptForm.fillTableSignal.emit(data)

            cursor.close()
            conn.close()
        except Exception as e:
            print(f'Hata: {e}')
    def ViewTranscriptTable(self):
        self.stuTranscriptForm.show()

    def load_teachers(self):
        query = "SELECT id, name, surname FROM academic_names"
        cursor = self.conn.cursor()
        cursor.execute(query)
        teachers = cursor.fetchall()

        # Öğretmenleri QComboBox'a koydum
        for teacher in teachers:
            full_name = f"{teacher[1]} {teacher[2]}"
            self.stuLoggedForm.comboBox_academics.addItem(full_name, teacher[0])

    def load_interests(self):
        query = "SELECT interest_id, interest_name FROM interests"
        cursor = self.conn.cursor()
        cursor.execute(query)
        interests = cursor.fetchall()

        for interest in interests:
            #full_name = f"{teacher[1]} {teacher[2]}"
            self.stuLoggedForm.comboBox_interests.addItem(interest[1], interest[0])