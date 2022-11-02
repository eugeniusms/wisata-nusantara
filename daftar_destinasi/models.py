from django.db import models
from django.contrib.auth.models import User

class Destinasi(models.Model):
  nama = models.CharField(max_length=255)
  deskripsi = models.TextField()
  lokasi = models.TextField()
  kategori = models.CharField(max_length=100)
  # add-ons
  foto_thumbnail_url = models.URLField()
  foto_cover_url = models.URLField()
  maps_url = models.URLField()
  jumlah_suka = models.IntegerField(default=0)
  # user related
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Suka(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  destinasi = models.ForeignKey(Destinasi, on_delete=models.CASCADE)