from django import forms
from .models import Destinasi

class AddDestinasiForm(forms.ModelForm):
  class Meta:
    model = Destinasi
    fields = ['nama','deskripsi','lokasi','kategori','foto_thumbnail_url','foto_cover_url','maps_url']