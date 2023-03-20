#llamamos al modelo
from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """managers para el moelo autor
    La clase "AutorManager" es una subclase de "models.Manager", que es la clase base para todos los Managers en Django. La clase "AutorManager" define un nuevo método llamado "listar_autores" que devuelve una lista de todos los autores en la base de datos.
    
    El método "listar_autores" simplemente llama al método "all()" del Manager, que devuelve todos los objetos del modelo "Autor" que se encuentran en la base de datos.
    
    
    
    """
    
    def buscar_autores(self, kword):
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        nombres = self.filter(
            nombre__icontains=kword
        )
        return nombres
    
    def buscar_autores2(self, kword):
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        nombres = self.filter(
            Q(nombre__icontains=kword) or Q(nombre__icontains=kword)
        )
        return nombres
    
    def buscar_autores2(self, kword):
        #mientras que el segundo utiliza un Manager personalizado llamado "AutorManager" definido en la clase "AutorManager".        
        nombres = self.filter(
            Q(nombre__icontains=kword) or Q(nombre__icontains=kword)
        )
        return nombres
    
    #excluye de la lista a los que tengan 
    def buscar_autores3(self, kword):
        nombres = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad=26) | Q(edad=50)
              )
        return nombres
    
    def buscar_autores4(self, kword):
        nombres = self.filter(
            edad__gt=40
        )
        return nombres