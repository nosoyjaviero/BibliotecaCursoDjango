from django.db import models
from  apps.autor.models import Autor
from .managers import LibroManager, CategoriaManager
# Create your models here.
    
class Categoria(models.Model):
    nombre =models.CharField("", max_length=50)
    
    objects= CategoriaManager()
    def __str__(self):
        return str(self.id) + " " +self.nombre 

    
class Libro(models.Model):
    titulo =models.CharField("Titulo", max_length=50)
    
    categoria  =models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    
    autores =models.ManyToManyField(Autor)
    
    portada= models.ImageField(upload_to='portada', null=True, blank=True)
    
    fecha_lanzamiento=models.DateField( 'Fecha de Lanzamiento')
    
    visitas=models.PositiveIntegerField("Visitas")
    
    objects= LibroManager()
    
    class Meta:
        verbose_name=''
        verbose_name_plural=''
        ordering = ['titulo','fecha_lanzamiento']
    
    def __str__(self):
        return str(self.id)+" - "+ self.titulo