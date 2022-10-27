from django.urls import path
from cerita_perjalanan.views import submit
from cerita_perjalanan.views import get

app_name = 'cerita_perjalanan'

urlpatterns = [
    path('/submit-review', submit, name='submit-review'),
    path('/get-review', get, name='get-review'),
]