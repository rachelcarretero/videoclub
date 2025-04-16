from django.urls import path
from . import views

#aqui estas llamando a vistas 

urlpatterns = [
    path("", views.getestrenos, name="estrenos"),  # /catalogo/
    path("listado/", views.getlistado, name="listado"),  # /catalogo/listado/
    path("detalle/<int:id>/", views.getdetalle, name="detalle"),  # /catalogo/detalle/1/
]

