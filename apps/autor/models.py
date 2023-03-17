from django.db import models
# Create your models here.
from .managers import AutorManager

class Autor(models.Model):
    nombre =models.CharField("Nombre", max_length=50)
    apellidos =models.CharField("Apellidos", max_length=50)
    nacionalidad =models.CharField("Nacionalidad", max_length=50)
    edad= models.PositiveIntegerField('Edad',)
    
    objects= AutorManager()
    
    def __str__(self):
        return self.nombre + " " + self.apellidos

