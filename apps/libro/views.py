from django.shortcuts import render

from .models import Libro
from django.views.generic import ListView



class LibrosListView(ListView):
    template_name = "libro/lista_libros.html"
    context_object_name= 'lista_libros'
    
    def get_queryset(self):        
        palabra= self.request.GET.get( "kword", "")               
        fecha1= self.request.GET.get( "date1", "")               
        fecha2= self.request.GET.get( "date2", "")       
          
        if fecha1  and fecha2:
                 
            return Libro.objects.buscar_libros2(palabra,fecha1,fecha2)
        else:
            return Libro.objects.buscar_libros(palabra)
