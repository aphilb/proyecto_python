from django.urls import path
from AppDatos import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('automoviles/', views.automoviles, name="Autos"),
    path('camioneta/', views.camionetas, name="Camionetas"),
    path('moto/', views.motos, name="Motos"),
    path('automovilesFormulario/', views.automoviles, name="AutosFormulario"),
    path('buscar/', views.buscar, name="Buscar"),
]