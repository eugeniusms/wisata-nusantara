from django.urls import path
from daftar_event.views import daftar_event

app_name = 'event'

urlpatterns = [
    path('', daftar_event, name='daftar_event'),
]