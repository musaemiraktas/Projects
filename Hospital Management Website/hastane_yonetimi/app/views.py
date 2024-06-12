import os
import random
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import connection
import requests
from .models import UZMANLIK_ALANLARI, Hasta, Doktor, Yonetici, Randevu, Rapor
from .forms import DoktorForm, HastaForm, RaporForm
from django.utils import timezone
import cloudinary.uploader
import json
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def anasayfa(request):
    return render(request, 'anasayfa.html')

def hasta_giris(request):
    if request.method == 'POST':
        telefon = request.POST.get('telefon')
        sifre = request.POST.get('sifre')
        with connection.cursor() as cursor:
            cursor.execute('SELECT hasta_id FROM hasta WHERE telefon = %s AND sifre = %s', [telefon, sifre])
            row = cursor.fetchone()
            if row:
                request.session['hasta_id'] = row[0]
                return redirect('hasta_sayfasi')
            else:
                messages.error(request, 'Geçersiz giriş bilgileri!')
    return render(request, 'hasta_giris.html')

def doktor_giris(request):
    if request.method == 'POST':
        telefon = request.POST.get('telefon')
        sifre = request.POST.get('sifre')
        with connection.cursor() as cursor:
            cursor.execute('SELECT doktor_id FROM doktor WHERE telefon = %s AND sifre = %s', [telefon, sifre])
            row = cursor.fetchone()
            if row:
                request.session['doktor_id'] = row[0]
                return redirect('doktor_sayfasi')
            else:
                messages.error(request, 'Geçersiz giriş bilgileri!')
    return render(request, 'doktor_giris.html')

def yonetici_giris(request):
    if request.method == 'POST':
        telefon = request.POST.get('telefon')
        sifre = request.POST.get('sifre')
        with connection.cursor() as cursor:
            cursor.execute('SELECT yonetici_id FROM yonetici WHERE telefon = %s AND sifre = %s', [telefon, sifre])
            row = cursor.fetchone()
            if row:
                request.session['yonetici_id'] = row[0]
                return redirect('yonetici_sayfasi')
            else:
                messages.error(request, 'Geçersiz giriş bilgileri!')
    return render(request, 'yonetici_giris.html')

def hasta_kayit(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        sifre = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO hasta (ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre])
        
        return render(request, 'hasta_giris.html')
    return render(request, 'hasta_kayit.html')

def doktor_kayit(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        uzmanlik_alani = request.POST.get('uzmanlik_alani')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        calistigi_hastane = request.POST.get('calistigi_hastane')
        sifre = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO doktor (ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, sifre) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', [ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, sifre])
        
        return render(request, 'doktor_giris.html')
    return render(request, 'doktor_kayit.html')

def hasta_sayfasi(request):
    hasta_id = request.session.get('hasta_id')
    if not hasta_id:
        return redirect('hasta_giris')

    if request.method == 'POST':
        form = HastaForm(request.POST)
        if form.is_valid():
            ad = form.cleaned_data['ad']
            soyad = form.cleaned_data['soyad']
            dogum_tarihi = form.cleaned_data['dogum_tarihi']
            cinsiyet = form.cleaned_data['cinsiyet']
            telefon = form.cleaned_data['telefon']
            adres = form.cleaned_data['adres']
            sifre = form.cleaned_data['sifre']

            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE hasta
                    SET ad = %s, soyad = %s, dogum_tarihi = %s, cinsiyet = %s, telefon = %s, adres = %s, sifre = %s
                    WHERE hasta_id = %s
                ''', [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre, hasta_id])

            return redirect('hasta_sayfasi')
    else:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM hasta WHERE hasta_id = %s', [hasta_id])
            hasta = dictfetchall(cursor)[0]
            form = HastaForm(initial={
                'ad': hasta['ad'],
                'soyad': hasta['soyad'],
                'dogum_tarihi': hasta['dogum_tarihi'],
                'cinsiyet': hasta['cinsiyet'],
                'telefon': hasta['telefon'],
                'adres': hasta['adres'],
                'sifre': hasta['sifre'],
            })

    return render(request, 'hasta_sayfasi.html', {'form': form, 'hasta': hasta})


def yonetici_sayfasi(request):
    yonetici_id = request.session.get('yonetici_id')
    if not yonetici_id:
        return redirect('yonetici_giris')

    isimler = ['Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Hasan','Namık','Selin']
    soyisimler = ['Yılmaz', 'Kaya', 'Demir', 'Çelik', 'Şahin','Ercan','Aktaş']
    sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana', 'Konya', 'Gaziantep', 'Şanlıurfa', 'Kocaeli']

    if request.method == 'POST':
        if 'ekle_hasta_doktor' in request.POST:
            for i in range(5):
                # Rastgele isim, soyisim ve şehir seçimi
                random_ad = random.choice(isimler)
                random_soyad = random.choice(soyisimler)
                random_dogum_tarihi = f'{random.randint(1950, 2010)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}'
                random_cinsiyet = random.choice(['Erkek', 'Kadın'])
                random_telefon = '+90' + ''.join(random.choices('0123456789', k=10))
                random_adres = random.choice(sehirler) 
                random_sifre = get_random_string(8)

                random_doktor_ad = random.choice(isimler)
                random_doktor_soyad = random.choice(soyisimler)
                random_uzmanlik_alani = random.choice([uzmanlik[0] for uzmanlik in UZMANLIK_ALANLARI])
                random_doktor_telefon = '+90' + ''.join(random.choices('0123456789', k=10))
                random_doktor_adres = random.choice(sehirler) 
                random_doktor_sifre = get_random_string(8)
                random_calistigi_hastane = 'Şehir Hastanesi'

                with connection.cursor() as cursor:
                    cursor.execute('''
                        INSERT INTO hasta (ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''', [random_ad, random_soyad, random_dogum_tarihi, random_cinsiyet, random_telefon, random_adres, random_sifre])

                    cursor.execute('''
                        INSERT INTO doktor (ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, sifre) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''', [random_doktor_ad, random_doktor_soyad, random_uzmanlik_alani, random_doktor_telefon, random_doktor_adres, random_calistigi_hastane, random_doktor_sifre])

            messages.success(request, 'Rastgele 5 hasta ve doktor başarıyla oluşturuldu.')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM yonetici WHERE yonetici_id = %s', [yonetici_id])
        yonetici = dictfetchall(cursor)[0]
        cursor.execute('SELECT * FROM hasta')
        hastalar = dictfetchall(cursor)
        cursor.execute('SELECT * FROM doktor')
        doktorlar = dictfetchall(cursor)
    
    return render(request, 'yonetici_sayfasi.html', {'yonetici': yonetici, 'hastalar': hastalar, 'doktorlar': doktorlar})

def randevu_al(request):
    hasta_id = request.session.get('hasta_id')
    if not hasta_id:
        return redirect('hasta_giris')

    if request.method == 'POST':
        randevu_tarihi = request.POST.get('randevu_tarihi')
        randevu_saati = request.POST.get('randevu_saati')
        uzmanlik_alani = request.POST.get('uzmanlik_alani')
        doktor_id = request.POST.get('doktor_id')

        try:
            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO randevu (hasta_id, doktor_id, randevu_tarihi, randevu_saati)
                    VALUES (%s, %s, %s, %s)
                ''', [hasta_id, doktor_id, randevu_tarihi, randevu_saati])

            messages.success(request, 'Randevu başarıyla alındı.')
            return redirect('hasta_sayfasi')
        except Exception as e:
            messages.error(request, f'Randevu alma işlemi sırasında bir hata oluştu: {e}')

    uzmanlik_alanlari = UZMANLIK_ALANLARI

    with connection.cursor() as cursor:
        cursor.execute('SELECT doktor_id, ad, soyad FROM doktor')
        doktorlar = dictfetchall(cursor)

    return render(request, 'randevu_al.html', {'uzmanlik_alanlari': uzmanlik_alanlari, 'doktorlar': doktorlar})

def randevularim(request):
    hasta_id = request.session.get('hasta_id')
    if not hasta_id:
        return redirect('hasta_giris')

    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT randevu.*, doktor.ad, doktor.soyad 
            FROM randevu 
            JOIN doktor ON randevu.doktor_id = doktor.doktor_id 
            WHERE randevu.hasta_id = %s
        ''', [hasta_id])
        randevular = dictfetchall(cursor)
    return render(request, 'randevularim.html', {'randevular': randevular})

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def raporlarim(request):
    hasta_id = request.session.get('hasta_id')
    if not hasta_id:
        return redirect('hasta_giris')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM rapor WHERE hasta_id = %s', [hasta_id])
        raporlar = dictfetchall(cursor)
        
        # JSON verisini parse ederek resim URL'lerini ve diğer bilgileri çıkaralım
        for rapor in raporlar:
            rapor_json = json.loads(rapor['rapor_json'])
            rapor['icerik'] = rapor_json.get('icerik', '')
            rapor['resim_url'] = rapor_json.get('resim_url', '')

    return render(request, 'raporlarim.html', {'raporlar': raporlar})

def doktorlari_getir(request):
    uzmanlik_alani = request.GET.get('uzmanlik_alani')
    with connection.cursor() as cursor:
        cursor.execute('SELECT doktor_id, ad, soyad FROM doktor WHERE uzmanlik_alani = %s', [uzmanlik_alani])
        doktorlar = dictfetchall(cursor)
    doktor_list = [{'doktor_id': d['doktor_id'], 'ad': d['ad'], 'soyad': d['soyad'],'uzmanlik_alani':uzmanlik_alani} for d in doktorlar]
    return JsonResponse(doktor_list, safe=False)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def doktor_sayfasi(request):
    doktor_id = request.session.get('doktor_id')
    if not doktor_id:
        return redirect('doktor_giris')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM doktor WHERE doktor_id = %s', [doktor_id])
        doktor = dictfetchall(cursor)[0]  # Tek bir doktor döndüğü varsayımıyla

        cursor.execute('''
            SELECT randevu.*, hasta.ad, hasta.soyad 
            FROM randevu 
            JOIN hasta ON randevu.hasta_id = hasta.hasta_id 
            WHERE randevu.doktor_id = %s
        ''', [doktor_id])
        randevular = dictfetchall(cursor)
    
    # Hasta ID'lerini randevular listesinden al
    hasta_id_list = [randevu['hasta_id'] for randevu in randevular]

    # Formu oluştur ve doldur
    form = DoktorForm(initial=doktor)

    if request.method == 'POST':
        form = DoktorForm(request.POST)
        if form.is_valid():
            ad = form.cleaned_data['ad']
            soyad = form.cleaned_data['soyad']
            uzmanlik_alani = form.cleaned_data['uzmanlik_alani']
            telefon = form.cleaned_data['telefon']
            adres = form.cleaned_data['adres']
            calistigi_hastane = form.cleaned_data['calistigi_hastane']

            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE doktor 
                    SET ad = %s, soyad = %s, uzmanlik_alani = %s, telefon = %s, adres = %s, calistigi_hastane = %s
                    WHERE doktor_id = %s
                ''', [ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, doktor_id])

            return redirect('doktor_sayfasi')

    return render(request, 'doktor_sayfasi.html', {'randevular': randevular, 'doktor': doktor, 'form': form, 'hasta_id_list': hasta_id_list})

def hasta_randevu_ve_raporlar(request, hasta_id):
    doktor_id = request.session.get('doktor_id')
    if not doktor_id:
        return redirect('doktor_giris')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM hasta WHERE hasta_id = %s', [hasta_id])
        hasta = dictfetchall(cursor)[0]
        
        cursor.execute('''
            SELECT randevu.*, doktor.ad, doktor.soyad 
            FROM randevu 
            JOIN doktor ON randevu.doktor_id = doktor.doktor_id 
            WHERE randevu.hasta_id = %s
        ''', [hasta_id])
        randevular = dictfetchall(cursor)

        cursor.execute('SELECT * FROM rapor WHERE hasta_id = %s', [hasta_id])
        raporlar = dictfetchall(cursor)

    return render(request, 'hasta_randevu_ve_raporlar.html', {'hasta': hasta, 'randevular': randevular, 'raporlar': raporlar})

def doktor_rapor_ekle(request, hasta_id):
    doktor_id = request.session.get('doktor_id')
    if not doktor_id:
        return redirect('doktor_giris')

    if request.method == 'POST':
        form = RaporForm(request.POST, request.FILES)
        if form.is_valid():
            rapor_icerigi = form.cleaned_data['rapor_icerigi']
            rapor_resmi = form.cleaned_data['rapor_resmi']

            # Cloudinary'ye yükleme
            upload_result = cloudinary.uploader.upload(rapor_resmi)
            rapor_resmi_url = upload_result['url']
            rapor_resmi_path = upload_result['public_id']

            # Özel formatta veritabanına kaydetme
            formatted_rapor_resmi = f"media/raporlar/{rapor_resmi_path}"
            formatted_rapor_json = json.dumps({
                "icerik": rapor_icerigi,
                "resim_url": rapor_resmi_url
            })

            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO rapor (hasta_id, doktor_id, rapor_tarihi, rapor_icerigi, rapor_resmi, rapor_json) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                ''', [hasta_id, doktor_id, timezone.now(), rapor_icerigi, formatted_rapor_resmi, formatted_rapor_json])

            return redirect('hasta_randevu_ve_raporlar', hasta_id=hasta_id)
    else:
        form = RaporForm()

    return render(request, 'doktor_rapor_ekle.html', {'form': form, 'hasta_id': hasta_id})







@csrf_exempt

def rapor_ekle(request):
    hasta_id = request.session.get('hasta_id')
    if not hasta_id:
        return JsonResponse({'success': False, 'error': 'Hasta girişi gerekli'})

    if request.method == 'POST':
        form = RaporForm(request.POST, request.FILES)
        if form.is_valid():
            rapor_icerigi = form.cleaned_data['rapor_icerigi']
            rapor_resmi = form.cleaned_data['rapor_resmi']

            # Cloudinary'ye yükleme
            upload_result = cloudinary.uploader.upload(rapor_resmi)
            rapor_resmi_url = upload_result['url']
            rapor_resmi_path = upload_result['public_id']

            # Özel formatta veritabanına kaydetme
            formatted_rapor_resmi = f"media/raporlar/{rapor_resmi_path}"
            formatted_rapor_json = json.dumps({
                "icerik": rapor_icerigi,
                "resim_url": rapor_resmi_url
            })

            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO rapor (hasta_id, rapor_tarihi, rapor_icerigi, rapor_resmi, rapor_json) 
                    VALUES (%s, %s, %s, %s, %s)
                ''', [
                    hasta_id, timezone.now(), 
                    rapor_icerigi, formatted_rapor_resmi, formatted_rapor_json
                ])

            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'error': 'Form geçerli değil'})

    form = RaporForm()
    return render(request, 'rapor_ekle.html', {'form': form})




def rapor_detay(request, rapor_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM rapor WHERE rapor_id = %s', [rapor_id])
        rapor = dictfetchall(cursor)[0]

        # JSON verisini parse ederek resim URL'sini ve diğer bilgileri çıkaralım
        rapor_json = json.loads(rapor['rapor_json'])
        rapor['icerik'] = rapor_json.get('icerik', '')
        rapor['resim_url'] = rapor_json.get('resim_url', '')

    return render(request, 'rapor_detay.html', {'rapor': rapor})

def rapor_indir(request, rapor_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM rapor WHERE rapor_id = %s', [rapor_id])
        rapor = dictfetchall(cursor)[0]

        # JSON verisini parse ederek resim dosyasının yolunu çıkaralım
        rapor_json = json.loads(rapor['rapor_json'])
        resim_url = rapor_json.get('resim_url', '')

    if resim_url:
        if resim_url.startswith(('http://', 'https://')):
            # Dış URL için indirme işlemi
            response = requests.get(resim_url)
            if response.status_code == 200:
                file_name = resim_url.split('/')[-1]
                response = HttpResponse(response.content, content_type='application/force-download')
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
            else:
                return HttpResponse("Dosya bulunamadı", status=404)
        else:
            # Yerel dosya yolu için indirme işlemi
            file_name = resim_url.split('/')[-1]
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/force-download')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                    return response
            else:
                return HttpResponse("Dosya bulunamadı", status=404)
    else:
        return HttpResponse("Resim URL'i bulunamadı", status=404)
    

def hasta_sil(request, hasta_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM hasta WHERE hasta_id = %s', [hasta_id])
        messages.success(request, 'Hasta başarıyla silindi.')
        return redirect('yonetici_sayfasi')
    return redirect('yonetici_sayfasi')

def doktor_sil(request, doktor_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM doktor WHERE doktor_id = %s', [doktor_id])
        messages.success(request, 'Doktor başarıyla silindi.')
        return redirect('yonetici_sayfasi')
    return redirect('yonetici_sayfasi')

def yonetici_hasta_detay(request, hasta_id):
    yonetici_id = request.session.get('yonetici_id')
    if not yonetici_id:
        return redirect('yonetici_giris')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM hasta WHERE hasta_id = %s', [hasta_id])
        hasta = dictfetchall(cursor)[0]
        cursor.execute('''
            SELECT randevu.*, doktor.ad, doktor.soyad 
            FROM randevu 
            JOIN doktor ON randevu.doktor_id = doktor.doktor_id 
            WHERE randevu.hasta_id = %s
        ''', [hasta_id])
        randevular = dictfetchall(cursor)
        cursor.execute('SELECT * FROM rapor WHERE hasta_id = %s', [hasta_id])
        raporlar = dictfetchall(cursor)
    return render(request, 'yonetici_hasta_detay.html', {'hasta': hasta, 'randevular': randevular, 'raporlar': raporlar})

def yonetici_rapor_ekle(request, hasta_id):
    yonetici_id = request.session.get('yonetici_id')
    if not yonetici_id:
        return redirect('yonetici_giris')

    if request.method == 'POST':
        form = RaporForm(request.POST, request.FILES)
        if form.is_valid():
            rapor_icerigi = form.cleaned_data['rapor_icerigi']
            rapor_resmi = form.cleaned_data['rapor_resmi']

            # Cloudinary'ye yükleme
            upload_result = cloudinary.uploader.upload(rapor_resmi)
            rapor_resmi_url = upload_result['url']
            rapor_resmi_path = upload_result['public_id']

            # Özel formatta veritabanına kaydetme
            formatted_rapor_resmi = f"media/raporlar/{rapor_resmi_path}"
            formatted_rapor_json = json.dumps({
                "icerik": rapor_icerigi,
                "resim_url": rapor_resmi_url
            })

            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO rapor (hasta_id, rapor_tarihi, rapor_icerigi, rapor_resmi, rapor_json) 
                    VALUES (%s, %s, %s, %s, %s)
                ''', [hasta_id, timezone.now(), rapor_icerigi, formatted_rapor_resmi, formatted_rapor_json])

            return redirect('yonetici_hasta_detay', hasta_id=hasta_id)
    else:
        form = RaporForm()

    return render(request, 'yonetici_rapor_ekle.html', {'form': form, 'hasta_id': hasta_id})

def doktor_detay(request, doktor_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM doktor WHERE doktor_id = %s', [doktor_id])
        doktor = dictfetchall(cursor)[0]
    return render(request, 'doktor_detay.html', {'doktor': doktor})

def yonetici_hasta_ekle(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        dogum_tarihi = request.POST.get('dogum_tarihi')
        cinsiyet = request.POST.get('cinsiyet')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        sifre = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO hasta (ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', [ad, soyad, dogum_tarihi, cinsiyet, telefon, adres, sifre])
        
        messages.success(request, 'Yeni hasta başarıyla eklendi.')
        return redirect('yonetici_sayfasi')
    
    return render(request, 'yonetici_hasta_ekle.html')

def yonetici_doktor_ekle(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        uzmanlik_alani = request.POST.get('uzmanlik_alani')
        telefon = request.POST.get('telefon')
        adres = request.POST.get('adres')
        calistigi_hastane = request.POST.get('calistigi_hastane')
        sifre = request.POST.get('sifre')

        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO doktor (ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, sifre) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', [ad, soyad, uzmanlik_alani, telefon, adres, calistigi_hastane, sifre])
        
        messages.success(request, 'Yeni doktor başarıyla eklendi.')
        return redirect('yonetici_sayfasi')
    
    return render(request, 'yonetici_doktor_ekle.html')
