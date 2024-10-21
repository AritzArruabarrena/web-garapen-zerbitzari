from django.urls import path
from . import views
urlpatterns = [
    path('', views.notak_list, name="default"),
    path('ikasle/new/', views.ikasle_new, name='zerrenda-ikasle-new'),
    path('ikasgai/new/', views.ikasgai_new, name='zerrenda-ikasgai-new'),
    path('notak/new/', views.notak_new, name='zerrenda-notak-new'),
    path('notak/editatu/<int:ikasle_id>/<int:ikasgai_id>/', views.notakEditatu_new, name="notak_editatu"),
    path('notak/ezabatu/<int:ikasle_id>/', views.ikasleaEzabatu, name="ikaslea_ezabatu"),
    path('logout/', views.logout_view, name="logout")  # Added a name for the logout view
]
