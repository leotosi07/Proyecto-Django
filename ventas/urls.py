from django.urls import path
from ventas import views


app_name= 'ventas'

urlpatterns = [
    path('',views.index, name='index'),
]
