from django.urls import path
from .views import listar_clientes, listar_productos

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('productos/', listar_productos, name='listar_productos'),
]
