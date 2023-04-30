from django.urls import path
from ventas import views


app_name= 'ventas'

urlpatterns = [
    path('',views.index, name='index'),
    path('animales/',views.AnimalListView.as_view(), name='lista_animales'),
    path('animales/crear',views.AnimalListView.as_view(), name='lista_animales'),    
    path('animales/<int:pk>/modificar',views.AnimalUpdateView.as_view(), name='modificar_animales'),
    path('animales/<int:pk>/eliminar',views.AnimalUpdateView.as_view(), name='eliminar_animales'),
    path('categorias/',views.CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/crear',views.CategoriaListView.as_view(), name='lista_categorias'),    
    path('categorias/<int:pk>/modificar',views.CategoriaUpdateView.as_view(), name='modificar_categorias'),
    path('categorias/<int:pk>/eliminar',views.CategoriaUpdateView.as_view(), name='eliminar_categorias'),
    path('tipos/',views.TipoListView.as_view(), name='lista_tipos'),
    path('tipos/crear',views.TipoListView.as_view(), name='lista_tipos'),    
    path('tipos/<int:pk>/modificar',views.TipoUpdateView.as_view(), name='modificar_tipos'),
    path('tipos/<int:pk>/eliminar',views.TipoUpdateView.as_view(), name='eliminar_tipos'),
    path('productos/',views.ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear',views.ProductoListView.as_view(), name='lista_productos'),    
    path('productos/<int:pk>',views.ProductoDetailView.as_view(), name='detalle_productos'),    
    path('productos/<int:pk>/modificar',views.ProductoUpdateView.as_view(), name='modificar_productos'),
    path('productos/<int:pk>/eliminar',views.ProductoUpdateView.as_view(), name='eliminar_productos'),
    path('comentarios/',views.ComentarioListView.as_view(), name='lista_comentarios'),
    path('comentarios/crear',views.ComentarioListView.as_view(), name='lista_comentarios'),    
    path('comentarios/<int:pk>',views.ComentarioDetailView.as_view(), name='detalle_comentarios'),    
    path('comentarios/<int:pk>/modificar',views.ComentarioUpdateView.as_view(), name='modificar_comentarios'),
    path('comentarios/<int:pk>/eliminar',views.ComentarioUpdateView.as_view(), name='eliminar_comentarios'),
]
