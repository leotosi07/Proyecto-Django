from django import forms
from django.forms import DateInput
from django.utils import timezone



class CreacionMascotaForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    especie = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'value': timezone.now().strftime('%Y-%m-%d')}),
    )
    propietario = forms.CharField(max_length=20)
    contacto_telefonico = forms.CharField(max_length=30)
    
class BuscarMascota(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)