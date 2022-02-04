from django.db import models

# Create your models here.
class usuarios(models.Model):
    codigo=models.CharField(max_length=500) 
    nombre=models.CharField(max_length=500) 
    puesto=models.CharField(max_length=500)

class marcajes(models.Model):
    codigo=models.CharField(max_length=500)
    fecha=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
