from django.urls import path
from daftar_destinasi.views import daftar_destinasi, show_json, show_suka_json, hapus_destinasi_by_id, show_suka_json, sukai_destinasi, show_wishlist, add_destination_flutter

app_name = 'daftar_destinasi'

urlpatterns = [
    path('', daftar_destinasi, name='daftar_destinasi'), # CREATE & READ
    path('json/', show_json, name='show_json'),
    path('suka/json/', show_suka_json, name='show_suka_json'),
    path('suka/<int:id>', sukai_destinasi, name='sukai_destinasi'), # UPDATE
    path('delete/<int:id>', hapus_destinasi_by_id, name='hapus_destinasi_by_id'),
    path('wishlist/', show_wishlist, name='show_wishlist'), # GET
    path('add-flutter/', add_destination_flutter, name='add_destination_flutter')
]