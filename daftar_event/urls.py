from django.urls import path
<<<<<<< HEAD
from daftar_event.views import add_json, category_event, daftar_event, show_json,delete_event,lihat_event, tambah_event,delete_all
=======
from daftar_event.views import daftar_event, tambah_event, show_json,delete_task,lihat_event
>>>>>>> aabee72c4de4398d109de33223c0dd88e29f1373

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_event, name='daftar_event'),
<<<<<<< HEAD
    path('show/<cat>', category_event, name='category_event'),
    path('tambah-event/', tambah_event, name='tambah-event'),
    path('json/',show_json, name='show_json'),
    path('add/',add_json, name='add_json'),
    path('delete/<id>', delete_event, name='delete-event'),
    path('show-event/<id>',lihat_event, name='lihat-event'),
    path('delete/', delete_all, name='delete')
=======
    path('tambah-event/', tambah_event, name='tambah-event'),
    path('json/',show_json, name='show_json'),
    path('delete-task/<id>', delete_task, name='delete-task'),
    path('event/<id>',lihat_event, name='lihat-event')
>>>>>>> aabee72c4de4398d109de33223c0dd88e29f1373
]