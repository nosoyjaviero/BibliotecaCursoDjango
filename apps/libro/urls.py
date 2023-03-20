from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("lista-libros", views.LibrosListView.as_view(), name="lista_libros"),
]