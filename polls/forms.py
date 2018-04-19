from django import forms
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Archivo, Trader, Portafolio, Sistema


class CargarArchivo(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = [
            "ruta",
        ]
class CrearTrader(forms.ModelForm):
    class Meta:
        model = Trader
        fields = [
            "username",
            "nombre",
            "apellido",
        ]
class CrearPortafolio(forms.ModelForm):
    class Meta:
        model = Portafolio
        fields = [
            "identificador",
            "nombre",
            "descripcion",
        ]
class CrearSistema(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = [
            "identificador",
            "nombre",
            "descripcion",
        ]
"""
    nombre: forms.CharField(widget=forms.TextInput(),required=True)
    file = forms.FileField()

class CargarArchivo(CreateView):
    model = Archivo
    fields = [
        "nombre",
        "file"
    ]

"""
