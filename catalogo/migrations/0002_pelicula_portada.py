# Generated by Django 5.2 on 2025-04-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='peliculas/'),
        ),
    ]
