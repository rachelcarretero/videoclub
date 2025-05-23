# Generated by Django 5.2 on 2025-04-08 12:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('anio', models.PositiveSmallIntegerField()),
                ('director', models.CharField(max_length=100)),
                ('formato', models.CharField(choices=[('VHS', 'VHS'), ('DVD', 'DVD'), ('BLU-RAY', 'Blu-ray')], max_length=10)),
                ('disponible', models.BooleanField(default=True)),
                ('generos', models.ManyToManyField(related_name='peliculas', to='catalogo.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alquiler', models.DateTimeField(auto_now_add=True)),
                ('fecha_devolucion', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.cliente')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.pelicula')),
            ],
        ),
    ]
