# catalogo/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def getestrenos(request):
    estrenos = Pelicula.objects.filter(anio=2019, disponible = True)
    return render(request, "catalogo/estrenos.html", {"listado_de_estrenos": estrenos})

def getlistado(request):
    todas = Pelicula.objects.all()
    return render(request, "catalogo/listado.html", {"todas": todas})

def getdetalle(request, id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request, "catalogo/detalle.html", {"detalle_de_pelicula": pelicula})
