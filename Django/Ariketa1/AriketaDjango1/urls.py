from django.urls import path
from . import views
urlpatterns = [
 #path('', views.ikasle_list , name="default"),
 path('', views.notak_list , name="default"),
 path('Ikasle/new/', views.ikasle_new, name='zerrenda-ikasle-new'),
 path('Ikasgai/new/', views.ikasgai_new, name='zerrenda-ikasgai-new'),
 path('Notak/new/', views.notak_new, name='zerrenda-notak-new'),
 path("Notak/editatu/<int:ikasle_id>/<int:ikasgai_id>/", views.notakEditatu_new, name="notak_editatu")
 
]