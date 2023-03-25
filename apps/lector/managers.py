from django.db import models
from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):
    
    def promedio_de_edad_en_libro(self):
        """Devuelve el promedio y la suma de las edades de los lectores que tomaron un determinado libro.

        Returns:
            resultados:
            El método devuelve un diccionario que contiene dos claves: promedio_edad y suma_edades, que contienen el promedio y la suma de las edades de los lectores que tomaron el libro especificado. Estos valores se obtienen a través de la función aggregate.
        """
        
        #El método usa el método filter para limitar los resultados a aquellos que pertenecen al libro con el id igual a 7. A continuación, utiliza el método aggregate para calcular el promedio y la suma de las edades de los lectores. La función Avg calcula el promedio y Sum calcula la suma.
        resultados=  self.filter(
            libro_id='7'
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edades= Sum('lector__edad')
        )
        return resultados
    
    def Cantidad_de_mismo_libro_prestado(self):
        """
        Lo que hace es contar cuántas veces se ha prestado cada libro. Agrupa los préstamos por el campo libro, que es la llave foránea que hace referencia al modelo Libro, y cuenta cuántas veces aparece cada valor en esa columna.
        
        Esto se lea asi. 
        Dado el modelo de Prestamo, esta función busca los libro que encuentran en prestamo, y luego cuenta cuántas veces se ha prestado cada libro en prestamo y devuelve un queryset que contiene con los libros que aprecieron y el número de veces que ha sido prestado. 
        Returns:
                 self.values('libro') Nos devuelve los libros que enconntro en prestamo
                 
                 .annotate
                 La cantidad de veces que aparecio en prestamo
        """
        
        
        # Por asi decirlo, agrupa los libros que aparecen en el registro de prestamo y dice la cantidad de veces que aparecen.
        resultados=self.values('libro').annotate(
            num_libros_prestados=Count('libro'),
            titulo= Lower('libro__titulo')
            )
        for resultado in resultados:
            print('*'*10)
            print(resultado, resultado['num_libros_prestados'])
    
         
        return resultados
    