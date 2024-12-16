from django.urls import path
from . import views
from .api import api

urlpatterns = [
    path("", views.productos, name="productos"),
    path("registro/", views.registro, name="registro"),
    path("resultado/<int:code>/", views.resultado, name="resultado"),
    path('editar/<int:code>/', views.editar_producto, name='editar_producto'),
    path("logout/", views.log_out, name="logout"),
    path("api/", api.urls),
]