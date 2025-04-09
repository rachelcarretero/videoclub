from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /catalogo/
    path("listado/", views.listado, name="listado"),  # /catalogo/listado/
    path("detalle/<int:id>/", views.detalle, name="detalle"),  # /catalogo/detalle/1/
]

