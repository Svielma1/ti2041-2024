from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("resultado/", views.resultado, name="resultado"),
    path("consulta/", views.consulta, name="consulta"),
]