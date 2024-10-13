from django.urls import path
from . import views  # Importar las vistas desde Kotxeak

urlpatterns = [
    path('', views.alokatu_list,name="alokatu_list"),
    

    path('pertsona/', views.pertsona_datuak, name='pertsona-datuak'),
    
    path('kotxeak-view/', views.kotxeko_datuak, name='kotxeko-datuak'),
    
    #path('kotxeak-datuak-view/', views.kotxeko_datuak_ikusi, name='kotxeko-datuak-ikusi'),
    
    
    path('kotxeak-list/', views.kotxeko_datuak_list,name='kotxeko-datuak-list'),
    
    
    path('base/', views.base_view, name="base_view") 
]
