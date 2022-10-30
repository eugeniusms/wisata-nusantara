from django.urls import path
from cerita_perjalanan.views import submit_review
from cerita_perjalanan.views import get_review

app_name = 'cerita_perjalanan'

urlpatterns = [
    path('/submit_review', submit_review, name='submit_review'),
    path('/get_review', get_review, name='get_review'),
]