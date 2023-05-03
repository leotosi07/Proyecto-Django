from django.contrib import admin
from ventas.models import Animal, Categoria,Tipo,Producto,Comentario
# Register your models here.
admin.site.register([Animal, Categoria,Tipo,Producto,Comentario])