# videoclub/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # asumiendo que en videoclub/views.py tienes la vista home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("catalogo/", include("catalogo.urls")),
]
