from django.db import models
from django.db.models import Q, Count, Avg, Sum

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
    
    
    