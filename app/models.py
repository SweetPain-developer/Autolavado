from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=120)
    Descripción = models.TextField(max_length=200, null=True)
    precio = models.IntegerField()
    stock  = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

class carruselImagene(models.Model):
    nombre = models.CharField(max_length=120)
    imagen = models.ImageField(upload_to="carrucel", null=False)

class Galeria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="galeria", null=False)

class MisionyVision(models.Model):
    titulo = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500, null=False)