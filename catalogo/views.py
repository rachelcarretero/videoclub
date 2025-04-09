# catalogo/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def estrenos(request):
    estrenos = Pelicula.objects.filter(anio=2019, disponible = True)
    return render(request, )

def listado(request):
    todas = Pelicula.objects.all()
    return render(request, "catalogo/listado.html", {"todas": todas})

def detalle(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, "catalogo/detalle.html", {"pelicula": pelicula})
