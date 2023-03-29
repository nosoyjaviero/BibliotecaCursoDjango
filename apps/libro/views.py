from django.shortcuts import render

from .models import Libro
from django.views.generic import ListView,DetailView



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

class LibrosListView_conTrigram(ListView):
    template_name = "libro/lista_libros.html"
    context_object_name= 'lista_libros'
    
    def get_queryset(self):        
        palabra= self.request.GET.get( "kword", "")
        
        return Libro.objects.buscar_libros_con_Trigram(palabra)
        
class FiltrarporCategoria(ListView):
    template_name = "libro/lista2.html"
    context_object_name= 'lista_libros'
    
    def get_queryset(self):       
        return Libro.objects.Listar_libros_categoria('6')
    
class LibroDetailView(DetailView):
    model =Libro
    template_name="libro/detalle.html"