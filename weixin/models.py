from django.db import models

# Create your models here.

class userInfo(models.Model):
    name=models.CharField(max_length=32)
    sex=models.CharField(max_length=32)
    email=models.CharField(max_length=32)
