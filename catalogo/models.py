from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    # Agrega mas campos si los necesitas, por ejemplo:
    # fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    FORMATO_CHOICES = (
        ('VHS', 'VHS'),
        ('DVD', 'DVD'),
        ('BLU-RAY', 'Blu-ray'),
    )

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    anio = models.PositiveSmallIntegerField()
    director = models.CharField(max_length=100)
    generos = models.ManyToManyField(Genero, related_name='peliculas')
    formato = models.CharField(max_length=10, choices=FORMATO_CHOICES)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo


class Alquiler(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_alquiler = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    # Campos extra si necesitas
    # por ejemplo: costo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Alquiler de {self.pelicula.titulo} a {self.cliente.user.username}"
