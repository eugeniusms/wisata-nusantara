from django.db import models

# Create your models here.
class Destinasi(models.Model):
  nama = models.CharField(max_length=255)
  deskripsi = models.TextField()
  lokasi = models.TextField()
  kategori = models.CharField(max_length=100)
  # add-ons
  foto_thumbnail_url = models.URLField()
  foto_cover_url = models.URLField()
  maps_url = models.URLField()
  suka = models.IntegerField(default=0)