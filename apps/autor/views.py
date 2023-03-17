from django.shortcuts import render

# Create your views here.
from .models import Autor
from django.views.generic import ListView



class ListAutores(ListView):
    model = Autor
    template_name = "autor/lista_autor.html"
    context_object_name= 'lista_autores'
