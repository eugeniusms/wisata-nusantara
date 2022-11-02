from django.db import models
class ceritaPerjalananItems(models.Model):
	name = models.CharField(max_length=100)
	review = models.TextField()