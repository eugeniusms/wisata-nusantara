from django.urls import path
from daftar_destinasi.views import daftar_destinasi, destinasi_by_id, show_json, tambah_destinasi, hapus_destinasi, hapus_destinasi_by_id

app_name = 'daftar_destinasi'

urlpatterns = [
    path('', daftar_destinasi, name='daftar_destinasi'),
    path('<int:id>', destinasi_by_id, name='destinasi_by_id'),
    path('json/', show_json, name='show_json'),
    path('add/', tambah_destinasi, name='tambah_destinasi'),
    path('delete/', hapus_destinasi, name='hapus_destinasi'),
    path('delete/<int:id>', hapus_destinasi_by_id, name='hapus_destinasi_by_id'),
]