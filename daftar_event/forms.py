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
<<<<<<< HEAD
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
=======
    'class' : 'form-control py-2 px-3 rounded-xl mb-2',
>>>>>>> aabee72c4de4398d109de33223c0dd88e29f1373
    'id' : 'nama',
  }
  lokasi_attrs = {
    'type' : 'text',
    'placeholder' : 'Location',
<<<<<<< HEAD
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
    'id' :'lokasi',
  }
  jenis_attrs = {
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
=======
    'class' : 'form-control py-2 px-3 rounded-xl mb-2',
    'id' :'lokasi',
  }
  jenis_attrs = {
    'class' : 'form-control py-2 px-3 rounded-xl mb-2',
>>>>>>> aabee72c4de4398d109de33223c0dd88e29f1373
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
<<<<<<< HEAD
    'class' : 'form-control py-2 px-3 rounded-xl mb-2 ml-4',
=======
    'class' : 'form-control py-2 px-3 rounded-xl mb-2',
>>>>>>> aabee72c4de4398d109de33223c0dd88e29f1373
    'rows' : '6',
    'cols' : '30', 
    'id' : 'deskripsi',
  }
  nama = forms.CharField(label="Name",required=True, max_length=255,widget=forms.TextInput(attrs=nama_attrs))
  lokasi = forms.CharField(label="Location",required=True, max_length=255,widget=forms.TextInput(attrs=lokasi_attrs))
  jenis = forms.ChoiceField(choices=event_choices,required=True,widget=forms.Select(attrs=jenis_attrs))
  deskripsi = forms.CharField(label="Deskripsi",required=True, max_length=255,widget=forms.Textarea(attrs=deskripsi_attrs))

