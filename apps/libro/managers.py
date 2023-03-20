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
    