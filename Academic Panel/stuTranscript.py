from PyQt5.QtWidgets import *
from stuTranscript_python import Ui_Form
from database import *
from PyQt5.QtCore import pyqtSignal



class StuTranscriptPage(QWidget):

    fillTableSignal = pyqtSignal(str)



    def __init__(self):
        super().__init__()
        self.stuTranscriptForm = Ui_Form()
        self.stuTranscriptForm.setupUi(self)

        self.fillTableSignal.connect(self.FillTable)



    def FillTable(self):
        conn = connect_to_database("postgres", "admin1234", "localhost", "5432", "yazlab1")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM transcript_info")
        rows = cursor.fetchall()
        # Tabloyu doldur
        for row in rows:
            self.stuTranscriptForm.tableWidget_transcript.insertRow(self.stuTranscriptForm.tableWidget_transcript.rowCount())
            for col_index, col_value in enumerate(row):
                item = QTableWidgetItem(str(col_value))
                self.stuTranscriptForm.tableWidget_transcript.setItem(self.stuTranscriptForm.tableWidget_transcript.rowCount() - 1, col_index, item)


        """conn.commit()
        conn.close()"""