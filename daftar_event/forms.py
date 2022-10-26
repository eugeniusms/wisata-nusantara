from django import forms
from django.forms import fields, widgets
from daftar_event.models import Event

class event_form(forms.ModelForm) :
  class Meta :
    model = Event
    fields = '__all__'

  nama_attrs = {
    'type' : 'text',
    'placeholder' : 'Nama Event',
    'class' : 'form-control'
  }
  lokasi_attrs = {
    'type' : 'text',
    'placeholder' : 'Lokasi',
    'class' : 'form-control'
  }
  jenis_attrs = {
    'class' : 'form-control'
  }
  event_choices = (
  ("Atraksi", "Atraksi"),
  ("Konser", "Konser"),
  ("Olahraga", "Olahraga"),
  ("Beauty", "Beauty"),
  )
  deskripsi_attrs = {
    'type' : 'text',
    'placeholder' : 'Harga',
    'class' : 'form-control'
  }
  nama = forms.CharField(label="Nama",required=True, max_length=255,widget=forms.TextInput(attrs=nama_attrs))
  lokasi = forms.CharField(label="Lokasi",required=True, max_length=255,widget=forms.TextInput(attrs=lokasi_attrs))
  jenis = forms.ChoiceField(choices=event_choices,required=True)
  deskripsi = forms.CharField(label="Deskripsi",required=True, max_length=255,widget=forms.TextInput(attrs=deskripsi_attrs))

