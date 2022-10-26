from django.urls import path
from daftar_destinasi.views import daftar_destinasi, show_json, tambah_destinasi

app_name = 'daftar_destinasi'

urlpatterns = [
    path('', daftar_destinasi, name='daftar_destinasi'),
    path('json/', show_json, name='show_json'),
    path('tambah/', tambah_destinasi, name='tambah_destinasi'),
]