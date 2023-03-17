#llamamos al modelo
from django.db import models

class AutorManager(models.Manager):
    """managers para el moelo autor
    La clase "AutorManager" es una subclase de "models.Manager", que es la clase base para todos los Managers en Django. La clase "AutorManager" define un nuevo método llamado "listar_autores" que devuelve una lista de todos los autores en la base de datos.
    
    El método "listar_autores" simplemente llama al método "all()" del Manager, que devuelve todos los objetos del modelo "Autor" que se encuentran en la base de datos.
    
    
    
    """
    
    def listar_autores(self):        
        return self.all()