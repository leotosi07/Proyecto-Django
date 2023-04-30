from django.db import models
from django.contrib.auth.models import User



class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    marca = models.CharField(max_length=50)
    fecha_de_carga = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario
    
class ItemDeCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Producto, through=ItemDeCarrito)