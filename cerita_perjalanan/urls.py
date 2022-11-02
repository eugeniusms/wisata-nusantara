from django.urls import path
from cerita_perjalanan.views import submit
from cerita_perjalanan.views import get

app_name = 'cerita_perjalanan'

urlpatterns = [
    path('', get, name='get'),
    path('submit/', submit, name='submit'),
]