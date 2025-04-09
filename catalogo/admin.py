from django.contrib import admin
from .models import Cliente, Pelicula, Genero, Alquiler

admin.site.register(Cliente)
admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Alquiler)
