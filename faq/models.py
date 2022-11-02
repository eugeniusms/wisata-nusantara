from statistics import mode
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class privateFaqData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    question = models.CharField(max_length=255)

class publicFaqData(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()