from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from ventas.models import Producto,Animal,Categoria,Tipo,Comentario


def index (request):
    return render (request,'ventas/tienda.html')

class ProductoListView(ListView):
    model = Producto
    template_name = "ventas/lista_productos.html"
    
class ProductoCreateView(CreateView):
    model = Producto
    template_name = "ventas/crear_productos.html"
    
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "ventas/editar_productos.html"    

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "ventas/borrar_productos.html"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "ventas/detalle_productos.html"

class AnimalListView(ListView):
    model = Animal
    template_name = "ventas/lista_animales.html"
    
class AnimalCreateView(CreateView):
    model = Animal
    template_name = "ventas/crear_animales.html"
    
class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = "ventas/editar_animales.html"    

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = "ventas/borrar_animales.html"
    
class CategoriaListView(ListView):
    model = Categoria
    template_name = "ventas/lista_categorias.html"
    
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "ventas/crear_categorias.html"
    
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "ventas/editar_categorias.html"    

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "ventas/borrar_categorias.html"

class TipoListView(ListView):
    model = Tipo
    template_name = "ventas/lista_tipos.html"
    
class TipoCreateView(CreateView):
    model = Tipo
    template_name = "ventas/crear_tipos.html"
    
class TipoUpdateView(UpdateView):
    model = Tipo
    template_name = "ventas/editar_tipos.html"    

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = "ventas/borrar_tipos.html"

class ComentarioListView(ListView):
    model = Comentario
    template_name = "ventas/lista_comentarios.html"
    
class ComentarioCreateView(CreateView):
    model = Comentario
    template_name = "ventas/crear_comentarios.html"
    
class ComentarioUpdateView(UpdateView):
    model = Comentario
    template_name = "ventas/editar_comentarios.html"    

class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = "ventas/borrar_comentarios.html"

class ComentarioDetailView(DetailView):
    model = Comentario
    template_name = "ventas/detalle_comentarios.html"



