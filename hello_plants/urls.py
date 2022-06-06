from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path(r'^log$', views.log, name="log"),
    path(r'^addplantpage$', views.addplantpage, name="addplantpage"),
    path("updateplants/<name>", views.updateplants, name="updateplants"),
    path('addplant/', views.addplant, name='addplant'),
    path('fertplants/<name>', views.fertplants, name='fertplants'), 
    path('delete/<int:plant_id>', views.delete, name='delete'),
]
