from django.urls import path
from . import views  # Importar las vistas desde Kotxeak

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal para Kotxeak
]
