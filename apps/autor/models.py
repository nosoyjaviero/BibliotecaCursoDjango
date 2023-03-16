from django.db import models
# Create your models here.


class Autor(models.Model):
    nombre =models.CharField("Nombre", max_length=50)
    apellidos =models.CharField("Apellidos", max_length=50)
    nacionalidad =models.CharField("Nacionalidad", max_length=50)
    edad= models.PositiveIntegerField('Edad',)
    
    def __str__(self):
        return self.nombre + " " + self.apellidos

