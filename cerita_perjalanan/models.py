from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ceritaPerjalananItems(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	review = models.TextField()

	def __str__(self):
		return self.name
