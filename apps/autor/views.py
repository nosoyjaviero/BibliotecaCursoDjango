from django.shortcuts import render

# Create your views here.
from .models import Autor
from django.views.generic import ListView



class ListAutores(ListView):
    template_name = "autor/lista_autor.html"
    context_object_name= 'lista_autores'
    
    def get_queryset(self):
        #devuelve todos los objetos del modelo "Autor" utilizando el Manager predeterminado de Django para ese modelo 
        palabra= self.request.GET.get( "kword", "")               
        return Autor.objects.buscar_autores(palabra)
    