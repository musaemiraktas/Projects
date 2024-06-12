from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

UZMANLIK_ALANLARI = [
    ('Dermatoloji', 'Dermatoloji'),
    ('Göğüs Hastalıkları', 'Göğüs Hastalıkları'),
    ('İç Hastalıkları', 'İç Hastalıkları'),
    ('Kardiyoloji', 'Kardiyoloji'),
    ('Nöroloji', 'Nöroloji'),
    ('Psikiyatri', 'Psikiyatri'),
    ('Genel Cerrahi', 'Genel Cerrahi'),
    ('Kulak Burun Boğaz', 'Kulak Burun Boğaz'),
    ('Kadın Hastalıkları ve Doğum', 'Kadın Hastalıkları ve Doğum'),
    ('Üroloji', 'Üroloji')
]

class Hasta(models.Model):
    hasta_id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    dogum_tarihi = models.DateField()
    cinsiyet = models.CharField(max_length=10, choices=(('Erkek', 'Erkek'), ('Kadın', 'Kadın'), ('Diğer', 'Diğer')))
    telefon = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon numarası formatı: '+999999999'. En fazla 15 rakam.")], default='0000000000')
    adres = models.TextField(default='N/A')
    sifre = models.CharField(max_length=100, default='temppass')

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class Doktor(models.Model):
    doktor_id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    uzmanlik_alani = models.CharField(max_length=50, choices=UZMANLIK_ALANLARI)
    telefon = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon numarası formatı: '+999999999'. En fazla 15 rakam.")], default='0000000000')
    adres = models.TextField(default='N/A')
    sifre = models.CharField(max_length=100, default='temppass')
    calistigi_hastane = models.CharField(max_length=200, default='N/A')

    def __str__(self):
        return f"{self.ad} {self.soyad} - {self.uzmanlik_alani} - {self.calistigi_hastane}"

class Yonetici(models.Model):
    yonetici_id = models.AutoField(primary_key=True)
    telefon = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon numarası formatı: '+999999999'. En fazla 15 rakam.")], unique=True)
    sifre = models.CharField(max_length=100)

    def __str__(self):
        return f"Yönetici {self.yonetici_id}"

class Randevu(models.Model):
    randevu_id = models.AutoField(primary_key=True)
    hasta = models.ForeignKey(Hasta, on_delete=models.CASCADE)
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    randevu_tarihi = models.DateField()
    randevu_saati = models.TimeField()

    def __str__(self):
        return f"{self.randevu_tarihi} - {self.randevu_saati} - {self.doktor.ad} {self.doktor.soyad}"


class Rapor(models.Model):
    rapor_id = models.AutoField(primary_key=True)
    hasta = models.ForeignKey(Hasta, on_delete=models.CASCADE)
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE, null=True, blank=True)  # Doktor alanını opsiyonel hale getirdik
    rapor_tarihi = models.DateTimeField(default=timezone.now)
    rapor_icerigi = models.TextField()
    rapor_resmi = models.ImageField(upload_to='raporlar/', blank=True, null=True)
    rapor_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Rapor {self.rapor_id} - {self.hasta.ad} {self.hasta.soyad} - {self.rapor_tarihi}"




