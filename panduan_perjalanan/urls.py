from django.urls import path
from panduan_perjalanan.views import get_perjalanan_json, panduan_perjalanan, add_perjalanan_json

app_name = 'panduan_perjalanan'

urlpatterns = [
    path("", panduan_perjalanan,name="panduan_perjalanan"),
    path("get_data/", get_perjalanan_json, name="get_perjalanan_json"),
    path("create_data/", add_perjalanan_json, name="add_perjalanan_json")
]