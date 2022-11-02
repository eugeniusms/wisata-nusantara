from django.urls import path
from cerita_perjalanan.views import submit_cerita, get_cerita, delete_cerita

app_name = 'cerita_perjalanan'

urlpatterns = [
    path('', get_cerita, name='get-cerita'),
    path('submit/', submit_cerita, name='submit-cerita'),
    path('delete/<int:id>', delete_cerita, name='delete-cerita')
]