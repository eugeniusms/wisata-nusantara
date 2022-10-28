from django.urls import path
from daftar_event.views import daftar_event, tambah_event, show_json,delete_task,lihat_event

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_event, name='daftar_event'),
    path('tambah-event/', tambah_event, name='tambah-event'),
    path('json/',show_json, name='show_json'),
    path('delete-task/<id>', delete_task, name='delete-task'),
    path('event/<id>',lihat_event, name='lihat-event')
]