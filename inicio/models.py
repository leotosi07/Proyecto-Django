from django.db import models



class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)