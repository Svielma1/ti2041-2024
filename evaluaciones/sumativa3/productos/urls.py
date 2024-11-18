from django.urls import path
from . import views

urlpatterns = [
    path("", views.productos, name="productos"),
    path("registro/", views.registro, name="registro"),
    path("resultado/<int:code>/", views.resultado, name="resultado"),
    path("logout/", views.log_out, name="logout"),
]