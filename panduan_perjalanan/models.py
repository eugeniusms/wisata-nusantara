from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class TujuanPerjalanan(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  kota_asal = models.CharField(max_length=100)
  kota_destinasi = models.CharField(max_length=100)
  date = models.DateField(auto_now_add= True)