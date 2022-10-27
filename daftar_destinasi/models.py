from django.db import models

# Create your models here.
class Destinasi(models.Model):
  nama = models.CharField(max_length=255)
  deskripsi = models.TextField()
  lokasi = models.TextField()
  kategori = models.CharField(max_length=100)