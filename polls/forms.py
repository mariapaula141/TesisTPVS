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
class TraderForm(forms.ModelForm):
     idtrader = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Identificador trader','id':'inputIdTrader'}))
     nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
     apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))
     class Meta:
          model = Dimtrader
          fields = ['idtrader','nombre','apellido']

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

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
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
