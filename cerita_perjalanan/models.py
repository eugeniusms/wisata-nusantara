from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class ceritaPerjalananItem(models.Model):
	name = models.CharField(max_length=100),
	# email = models.EmailField(),
	review = models.TextField(),

