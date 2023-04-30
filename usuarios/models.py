from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)
    
