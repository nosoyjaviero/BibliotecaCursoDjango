from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    """managers para el moelo libro
    
    """
    
    def buscar_libros(self, kword):
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        libros= self.filter(
            titulo__icontains=kword
        )
        return libros
    