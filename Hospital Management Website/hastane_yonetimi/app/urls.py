from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('hasta_giris/', views.hasta_giris, name='hasta_giris'),
    path('doktor_giris/', views.doktor_giris, name='doktor_giris'),
    path('yonetici_giris/', views.yonetici_giris, name='yonetici_giris'),
    path('hasta_kayit/', views.hasta_kayit, name='hasta_kayit'),
    path('doktor_kayit/', views.doktor_kayit, name='doktor_kayit'),
    path('hasta_sayfasi/', views.hasta_sayfasi, name='hasta_sayfasi'),
    path('randevu_al/', views.randevu_al, name='randevu_al'),
    path('randevularim/', views.randevularim, name='randevularim'),
    path('rapor_ekle/', views.rapor_ekle, name='rapor_ekle'),
    path('rapor_indir/<int:rapor_id>/', views.rapor_indir, name='rapor_indir'),
    path('raporlarim/', views.raporlarim, name='raporlarim'),
    path('doktor_sayfasi/', views.doktor_sayfasi, name='doktor_sayfasi'),
    path('yonetici_sayfasi/', views.yonetici_sayfasi, name='yonetici_sayfasi'),
    path('hasta_randevu_ve_raporlar/<int:hasta_id>/', views.hasta_randevu_ve_raporlar, name='hasta_randevu_ve_raporlar'),
    path('doktor_rapor_ekle/<int:hasta_id>/', views.doktor_rapor_ekle, name='doktor_rapor_ekle'),
    path('doktorlari_getir/', views.doktorlari_getir, name='doktorlari_getir'),
    path('rapor_detay/<int:rapor_id>/', views.rapor_detay, name='rapor_detay'),
    path('hasta_sil/<int:hasta_id>/', views.hasta_sil, name='hasta_sil'),
    path('doktor_sil/<int:doktor_id>/', views.doktor_sil, name='doktor_sil'),
    path('doktor_detay/<int:doktor_id>/', views.doktor_detay, name='doktor_detay'),
    path('yonetici_rapor_ekle/<int:hasta_id>/', views.yonetici_rapor_ekle, name='yonetici_rapor_ekle'),
    path('yonetici_doktor_ekle/', views.yonetici_doktor_ekle, name='yonetici_doktor_ekle'),  # Yeni URL
    path('yonetici_hasta_ekle/', views.yonetici_hasta_ekle, name='yonetici_hasta_ekle'),  # Yeni URL
    path('yonetici_hasta_detay/<int:hasta_id>/', views.yonetici_hasta_detay, name='yonetici_hasta_detay'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
