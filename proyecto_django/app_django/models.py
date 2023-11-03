from django.db import models

# Create your models here.
class alumnos(models.Model):
    codigo= models.CharField(max_length=10)
    nombre= models.CharField(max_length=65)
    telefono= models.CharField(max_length=9)
