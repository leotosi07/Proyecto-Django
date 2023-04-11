from django.db import models
from datetime import date


class Animal(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    propietario = models.CharField(max_length=20)
    contacto_telefonico = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now_add=True)