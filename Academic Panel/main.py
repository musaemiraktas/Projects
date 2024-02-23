import psycopg2
import random
import string

from PyQt5.QtWidgets import *
from anaPanel import MainPage
app = QApplication([])

conn = psycopg2.connect(
    dbname="yazlab1",
    user="postgres",
    password="admin1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

for i in range(1, 51):  # 1'den 50'ye kadar olan ID'leri ekleyin
    # Rastgele kullanıcı adı ve şifre oluşturma
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    # Veritabanına ekleme sorgusu
    #insert_query = "INSERT INTO students (id, username, password) VALUES (%s, %s, %s)"
    #cur.execute(insert_query, (i, username, password))

    update_query = "UPDATE students SET username = %s WHERE id = %s"
    update_query_pwd = "UPDATE students SET password = %s "
    #for i in range(1, 51):  # 1'den 50'ye kadar olan öğrencileri güncelle
    #    new_username = ''.join(random.choice(string.digits) for _ in range(6))
    #    cur.execute(update_query, (new_username, i))

# "students" tablosundaki öğrenci ID'lerini sorgulayın
cur.execute("SELECT id FROM students")
student_ids = [row[0] for row in cur.fetchall()]

# "isim" ve "soyisim" listelerini özelleştirilmiş isim verileriyle doldurun
names = ["Emir", "Can", "Ebru", "Zehra", "Efe", "Süheyla", "Enes", "Ayça"]
surnames = ["Razi", "Reis", "Demir", "Koç", "Öztürk", "Aydın", "Şahin", "Aktaş"]

# Yeni tabloyu oluşturmak için SQL sorgusu
#create_table_query = """
#CREATE TABLE student_names (
#    id SERIAL PRIMARY KEY,
#    student_id INTEGER,
#    isim VARCHAR(50),
#    soyisim VARCHAR(50)
#)
#"""
#cur.execute(create_table_query)

# Her öğrenci için rastgele isim ve soyisim ekleme
#insert_query = "INSERT INTO student_names (student_id, isim, soyisim) VALUES (%s, %s, %s)"
#for student_id in student_ids:
#    name = random.choice(names)
#    surname = random.choice(surnames)
#    cur.execute(insert_query, (student_id, name, surname))


# "id" sütununu silmek için SQL sorgusu
#alter_table_query = "ALTER TABLE student_names DROP COLUMN id"
#6cur.execute(alter_table_query)



# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

#Ana pencereyi çalıştırdım ve elle kapatılana kadar döngüde kalmasını sağladım.
pencere = MainPage()
pencere.show()
app.exec_()