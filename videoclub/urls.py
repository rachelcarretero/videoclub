# videoclub/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # asumiendo que en videoclub/views.py tienes la vista home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("catalogo/", include("catalogo.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


