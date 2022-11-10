from django.db import models

# Create your models here.
class Users(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password =models.CharField(max_length=50)