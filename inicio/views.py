from django.shortcuts import render
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from inicio.forms import CreacionMascotaForm,BuscarMascota
from inicio.models import Mascota


def inicio (request):
    return render (request,'inicio/index.html')

def buscar_mascota (request):
    return render (request,'inicio/buscar_mascota.html')

def cargar_mascota (request):
    if request.method == "POST":
        formulario = CreacionMascotaForm(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            mascota = Mascota(
                nombre=datos_correctos['nombre'], 
                especie=datos_correctos['especie'],
                raza = datos_correctos['raza'], 
                fecha_nacimiento = datos_correctos['fecha_nacimiento'], 
                )
            mascota.save()

            return redirect('inicio:buscar_mascota')
    
    formulario = CreacionMascotaForm()
    return render(request, 'inicio/cargar_mascota.html', {'formulario': formulario})

def buscar_mascota(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        mascotas = Mascota.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        mascotas = Mascota.objects.all()
        
    formulario_busqueda = BuscarMascota()
    
    return render(request, 'inicio/buscar_mascota.html', {'mascotas': mascotas, 'formulario': formulario_busqueda})

