from django.db import models

# Create your models here.
class clases(models.Model):
    nombre = models.CharField(max_length=30)
    tematica= models.CharField(max_length=30)