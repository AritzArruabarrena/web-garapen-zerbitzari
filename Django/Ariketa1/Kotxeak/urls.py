from django.urls import path
from . import views  # Importar las vistas desde Kotxeak

urlpatterns = [
    path('zerrenda', views.index, name='index'),  # Ruta principal para Kotxeak
    path('', views.alokatu_list,name="alokatu_list"),
    path("kotxeak/", views.kotxeko_datuak, name="kotxeko-datuak"),
    path('', views.index, name='index2'),
    path('pertsona/', views.pertsona_datuak, name='pertsona-datuak'),
    path('kotxeak/ikusi/', views.kotxeko_datuak_ikusi, name='kotxeko-datuak-ikusi'),
    path('kotxeak/', views.kotxeko_datuak_list,name="kotxeko_datuak_list"),
]
