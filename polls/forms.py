from django import forms
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import *

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class CargarArchivo(forms.ModelForm):

    class Meta:
        model = Archivo
        fields = [
            "ruta",
        ]
    def clean_recipients(self):
        data = self.cleaned_data['ruta']
        if ("Spot-fwd.csv" or "CURR_FUT.csv") not in data:
            raise forms.ValidationError("Archivo inválido")
        return data


class CrearContraparte(forms.ModelForm):
    idcontraparte = forms.CharField(label='Identificador Contraparte', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador Contraparte','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    #descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}))
    class Meta:
        model = Dimcontraparte
        fields = [
            "idcontraparte",
            "nombre"
        ]
class CrearEstado(forms.ModelForm):
    idestado = forms.CharField(label='Identificador estado', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador estado','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    class Meta:
        model = Dimestado
        fields = [
            "idestado",
            "nombre",
        ]

class CrearInfomoneda(forms.ModelForm):
    idmoneda = forms.CharField(label='Identificador moneda', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador moneda','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}))
    class Meta:
        model = Diminfomoneda
        fields = [
            "idmoneda",
            "nombre",
            "descripcion"
        ]

class CrearPortafolio(forms.ModelForm):
    idportafolio = forms.CharField(label='Identificador portafolio', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador portafolio','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}))
    class Meta:
        model = Dimportafolio
        fields = [
            "idportafolio",
            "nombre",
            "descripcion"
        ]


class CrearSistema(forms.ModelForm):
    idsistema = forms.CharField(label='Identificador sistema', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador sistema','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}))
    class Meta:
        model = Dimsistema
        fields = [
            "idsistema",
            "nombre",
            "descripcion"
        ]

class CrearTrader(forms.ModelForm):
     idtrader = forms.CharField(label='Identificador trader',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador trader','id':'inputId'}))
     nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
     apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))
     class Meta:
          model = Dimtrader
          fields = ['idtrader','nombre','apellido']

class CrearProducto(forms.ModelForm):
    idproducto = forms.CharField(label='Identificador producto', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador producto','id':'inputId'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    tipo_operacion = forms.CharField(label='Tipo operación', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tipo operación'}))
    class Meta:
        model = Dimproducto
        fields = [
            "idproducto",
            "nombre",
            "tipo_operacion"
        ]


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre usuario'}))
    first_name = forms.CharField(label='Nombres',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}))
    last_name = forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}))
    email=forms.EmailField(required=True,label='Correo electrónico',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'example@tpvs.com'}))
    password1=forms.CharField(required=True,label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))
    password2=forms.CharField(required=True,label='Confirmar contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar contraseña'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.firs_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre usuario'}))
    first_name = forms.CharField(label='Nombres',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}))
    last_name = forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}))
    email=forms.EmailField(label='Correo electrónico',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'example@tpvs.com'}))
    password=forms.CharField(label='',widget = forms.HiddenInput(), required = False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
class PasswordChangeForm(UserChangeForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
