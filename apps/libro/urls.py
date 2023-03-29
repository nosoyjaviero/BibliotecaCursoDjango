from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("lista-libros", views.LibrosListView.as_view(), name="lista_libros"),
     path("lista-libro2", views.LibrosListView_conTrigram.as_view(), name="lista_librosTrigram"),
     path("lista-2", views.FiltrarporCategoria.as_view(), name="lista_libros2"),
     path("libro-detalle/<pk>", views.LibroDetailView.as_view(), name="libro_detalle"),
     
]