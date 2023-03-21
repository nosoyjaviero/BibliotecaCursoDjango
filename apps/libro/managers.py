import datetime
from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    """managers para el moelo libro
    
    """
    
    def buscar_libros(self, kword):
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        libros= self.filter(
            titulo__icontains=kword,
        )
        return libros
    
    def buscar_libros2(self, kword, date1, date2):
        
        date1= datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        date2= datetime.datetime.strptime(date2, "%Y-%m-%d").date()
        
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        libros= self.filter(
            titulo__icontains=kword,
            fecha_lanzamiento__range=(date1,date2)
        )
        return libros
    
    def Listar_libros_categoria(self, categoria):
        
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
        
    def add_autor_libro(self, libro_id, autor):
        libro=self.get(id=libro_id)
        libro.autores.add(autor)
        return libro
    def delete_autor_libro(self, libro_id, autor):
        libro=self.get(id=libro_id)
        libro.autores.remove(autor)
        return libro
    
class CategoriaManager(models.Manager):
    """managers para el modelo Categoria
    
    """
    def categoria_por_autor(self, autor):
        
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()
    