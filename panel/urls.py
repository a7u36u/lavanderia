from django.contrib import admin
from django.urls import path, include

from django import views
from . import views
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    # path('', views.index, name="index"),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('home', home, name="home"),   
    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar', views.actualizar, name="actualizar"),
    path('eliminar', views.eliminar, name="eliminar"),
    path('listar_ropa', views.listar_ropa, name="listar_ropa"),
    path('agregar_ropa', views.agregar_ropa, name="agregar_ropa"),
    path('actualizar_ropa', views.actualizar_ropa, name="actualizar_ropa"),
    path('eliminar_ropa', views.eliminar_ropa, name="eliminar_ropa"),
     path("logout", logout, name="logout"),
]

