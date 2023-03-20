from django.shortcuts import render

from .models import Libro
from django.views.generic import ListView



class LibrosListView(ListView):
    template_name = "libro/lista_libros.html"
    context_object_name= 'lista_libros'
    
    def get_queryset(self):        
        palabra= self.request.GET.get( "kword", "")               
        return Libro.objects.buscar_libros(palabra)
