from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("updateplants/<name>", views.updateplants, name="updateplants")
]
