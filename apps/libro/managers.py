import datetime
from django.db import models
from django.db.models import Q, Count

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
    
    
    # Definimos un método llamado "numeros_De_Libros_Prestados" que recibe el parámetro "self" (representando la instancia de la clase que lo llama)
    
    def numeros_De_Libros_Prestados(self):
        """Método que realiza una consulta a la base de datos para obtener la cantidad de libros prestados.
        aggregate: devuelve un diccionario con el valor de la operacion aritmetica que hayamos especificado.

        Returns:
        dict: Un diccionario que contiene un campo "num_libros" con la cantidad de libros prestados.
        """
    # Usamos el método "aggregate" para realizar una consulta que cuenta la cantidad de libros prestados.
    # El resultado se almacena en la variable "resultados", que contiene un objeto con un campo "num_libros" que tiene la cantidad de libros prestados.
        resultados = self.aggregate(num_libros=Count('libro_prestamo'))
    
    # Retornamos el objeto "resultados".
        return resultados
    
class CategoriaManager(models.Manager):
    """managers para el modelo Categoria
    
    """
    def categoria_por_autor(self, autor):
        
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()
        
    # Definimos un método llamado "listar_cantidad_de_libros_categoria" que recibe el parámetro "self" (representando la instancia de la clase que lo llama)
    def listar_cantidad_de_libros_categoria(self):
        """Este método lista la cantidad de libros por una categoría.
        Este metodo se puede hacer utilizando una consulta de  base de Datos inluso utilizando solo utilando pyhon. Pero django nos la pone mas facil, y no deja este codigo para poder esta consulta

        Returns:
        annotate: devuelve un QuerySet y ademas la operacion aritmetica que estemos realizando.Puede verse en: print(resultado, resultado.num_libros)
        
        resultado (objeto): El último objeto resultado obtenido.
    """
        # Se utiliza el método "annotate" para realizar una consulta que obtiene la cantidad de libros por categoría.
        # El resultado se almacena en la variable "resultados", que contiene una lista de objetos con los campos de la clase y el número de libros por categoría.
        resultados = self.annotate(
            num_libros=Count('categoria_libro')
            )
        
        
        # Se recorre la lista de "resultados" con un ciclo "for" para imprimir cada objeto y su respectiva cantidad de libros.
        for resultado in resultados:
            print('*'*10)
            print(resultado, resultado.num_libros)
    
    # Retorna el último resultado obtenido.
        return resultado