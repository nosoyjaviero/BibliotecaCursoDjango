from django.db import models
from  apps.autor.models import Autor
from .managers import LibroManager
# Create your models here.
    
class Categoria(models.Model):
    nombre =models.CharField("", max_length=50)
    def __str__(self):
        return self.nombre 

    
class Libro(models.Model):
    titulo =models.CharField("Titulo", max_length=50)
    
    categoria  =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    autores =models.ManyToManyField(Autor)
    
    portada= models.ImageField(upload_to='portada', null=True, blank=True)
    
    fecha_lanzamiento=models.DateField( 'Fecha de Lanzamiento')
    
    visitas=models.PositiveIntegerField("Visitas")
    
    objects= LibroManager()
    
    def __str__(self):
        return self.titulo