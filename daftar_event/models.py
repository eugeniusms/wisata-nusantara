from django.db import models

# Create your models here.
class Event(models.Model):
  event_choices = (
  ("Atraksi", "Atraksi"),
  ("Konser", "Konser"),
  ("Olahraga", "Olahraga"),
  ("Beauty", "Beauty"),
  )
  nama = models.CharField(max_length = 255)
  lokasi = models.TextField()
  jenis = models.TextField(choices=event_choices, default=None)
  deskripsi = models.TextField()