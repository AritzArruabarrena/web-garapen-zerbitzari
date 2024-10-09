from django.urls import path
from . import views  # Importar las vistas desde Kotxeak

urlpatterns = [
    path('zerrenda/', views.index, name='index'),  # Ruta principal para Kotxeak
    path('', views.alokatu_list,name="alokatu_list")
]
