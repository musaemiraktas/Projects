import json
from django import forms
from .models import Rapor, Doktor, Hasta
from django.utils import timezone
from django.db import connection


class RaporForm(forms.ModelForm):
    class Meta:
        model = Rapor
        fields = ['rapor_icerigi', 'rapor_resmi']

    def save(self, commit=True):
        instance = super(RaporForm, self).save(commit=False)
        rapor_json = {'icerik': self.cleaned_data['rapor_icerigi']}
        if 'rapor_resmi' in self.cleaned_data and self.cleaned_data['rapor_resmi']:
            rapor_resmi = self.cleaned_data['rapor_resmi']
            instance.rapor_resmi = rapor_resmi
            rapor_json['resim_url'] = instance.rapor_resmi.name

        instance.rapor_json = json.dumps(rapor_json)  # JSON string olarak kaydet
        if commit:
            instance.save()
        return instance
    
class DoktorForm(forms.ModelForm):
    class Meta:
        model = Doktor
        fields = ['ad', 'soyad', 'uzmanlik_alani', 'telefon', 'adres', 'calistigi_hastane', 'sifre']

class HastaForm(forms.ModelForm):
    class Meta:
        model = Hasta
        fields = ['ad', 'soyad', 'dogum_tarihi', 'cinsiyet', 'telefon', 'adres', 'sifre']
