from django.urls import path

from daftar_event.views import add_json, category_event, daftar_event, show_json,delete_event,lihat_event, tambah_event, add_from_flutter, delete_from_flutter

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_event, name='daftar_event'),
    path('show/<cat>', category_event, name='category_event'),
    path('tambah-event/', tambah_event, name='tambah-event'),
    path('json/',show_json, name='show_json'),
    path('add/',add_json, name='add_json'),
    path('delete/<id>', delete_event, name='delete-event'),
    path('lihat-event/<id>',lihat_event, name='lihat-event'),
    path('add_from_flutter/', add_from_flutter, name='add_from_flutter'),
    path('delete_from_flutter/<id>', delete_from_flutter, name='delete_from_flutter')
]