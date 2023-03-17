from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("lista-autores", views.ListAutores.as_view(), name="lista_autores"),
]