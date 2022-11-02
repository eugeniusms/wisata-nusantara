from email.policy import default
from django import forms
from django.forms import fields, widgets
from daftar_event.models import Event

class event_form(forms.ModelForm) :
  class Meta :
    model = Event
    fields = '__all__'

  nama_attrs = {
    'type' : 'text',
    'placeholder' : 'Name',
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'id' : 'nama',
  }
  lokasi_attrs = {
    'type' : 'text',
    'placeholder' : 'Location',
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'id' :'lokasi',
    
  }
  jenis_attrs = {
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'id' : 'jenis',
  }
  event_choices = (
  ("Musik", "Musik"),
  ("Olahraga", "Olahraga"),
  ("Budaya", "Budaya"),
  ("Lainnya", "Lainnya"),
  )
  deskripsi_attrs = {
    'type' : 'text',
    'placeholder' : 'Description',
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'rows' : '6',
    'cols' : '30', 
    'id' : 'deskripsi',
  }
  foto_attrs = {
    'type' : 'url',
    'placeholder' : 'Photo URL',
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'id' :'foto',
  }
  
  nama = forms.CharField(label="Name",required=True, max_length=255,widget=forms.TextInput(attrs=nama_attrs))
  lokasi = forms.CharField(label="Location",required=True, max_length=255,widget=forms.TextInput(attrs=lokasi_attrs))
  jenis = forms.ChoiceField(choices=event_choices,required=True,widget=forms.Select(attrs=jenis_attrs))
  deskripsi = forms.CharField(label="Deskripsi",required=True, max_length=255,widget=forms.Textarea(attrs=deskripsi_attrs))
  foto = forms.URLField(label="Photo URL",required=True,widget=forms.URLInput(attrs=foto_attrs))
