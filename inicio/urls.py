from django.urls import path
from inicio import views


app_name= 'inicio'

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('buscar-mascota/',views.buscar_mascota, name='buscar_mascota'),
    path('cargar-mascota/',views.cargar_mascota, name='cargar_mascota'),
]
