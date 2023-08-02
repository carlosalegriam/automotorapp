from django.urls import path
from .views import index, add_vehiculo, listar_vehiculos, register, logout_user, login, inicio


urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('vehiculo/add/', add_vehiculo, name='add'),
    path('vehiculo/listar/', listar_vehiculos, name='listar'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]
