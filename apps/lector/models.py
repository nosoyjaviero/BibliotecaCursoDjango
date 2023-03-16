from django.db import models
from apps.libro.models import Libro

# Create your models here.

class Lector(models.Model):
    nombre=models.CharField("Nombre", max_length=50)
    apellidos=models.CharField("Apeliidos", max_length=50)
    nacionalidad=models.CharField("Nacionalidad", max_length=50)
    edad=models.IntegerField("Edad",default=0)
    
    
class Prestamo(models.Model):
    lector= models.ForeignKey(Lector, on_delete=models.CASCADE)    
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo=models.DateField("Fecha Prestamo")
    fecha_devolucion=models.DateField("Fecha Devolucion")
    Devuelto=models.BooleanField("Devuelto")