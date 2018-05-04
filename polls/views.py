from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Trader, Portafolio, Archivo, Sistema, Mensaje
from .forms import (
    CargarArchivo, CrearTrader,
    CrearPortafolio, CrearSistema,
    RegistrationForm, EditProfileForm
)
from django.utils import timezone
import tablib
from import_export import resources
from rest_framework import viewsets
from .serializers import MensajeSerializer
from webline_notifications.models import Notification
from django.contrib.auth.models import User

# Create your views here.


from django.http import HttpResponse

#API
class MensajeView(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    #falta guardar esto en el la base de datos

#Registro
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('esperar')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

#Espera
def esperar(request):
    return render(request,"esperar.html")

#Error
@login_required(login_url="login_view")
def error(request):
    return render(request,"error.html")


#Index
@login_required(login_url="login_view")
def index(request):
    notificaciones = Notification.objects.filter()
    usuario = request.user
    return render(request,"index.html", {'notificaciones':notificaciones, 'usuario':usuario})

#Logs
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = AuthenticationForm()


    return render(request,'login_view.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')




#Menu
@login_required(login_url="login_view")
def archivo(request):
    if request.method =='POST':
        form = CargarArchivo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.fecha = timezone.now()
            instance.save()
            return redirect('archivo')
    else:
        form = CargarArchivo()
    return render(request,"archivo.html",{'form':form})

@login_required(login_url="login_viw")
def contraparte(request):
    return render(request,"contraparte.html")

@login_required(login_url="login_view")
def estado(request):
    return render(request,"estado.html")

@login_required(login_url="login_view")
def portafolio(request):
    if request.method =='POST':
        form = CrearPortafolio(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.fecha = timezone.now()
            instance.save()
            return redirect('portafolio')
    else:
        form = CrearPortafolio()
    portafolios = Portafolio.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'portafolio.html', {'form': form, 'portafolios': portafolios})


@login_required(login_url="login_view")
def producto(request):
    return render(request,"producto.html")

@login_required(login_url="login_view")
def parMoneda(request):
    return render(request,"pares.html")

@login_required(login_url="login_view")
def info(request):
    return render(request,"info.html")

@login_required(login_url="login_view")
def trader(request):
    if request.method =='POST':
        form = CrearTrader(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.fecha = timezone.now()
            instance.save()
            return redirect('trader')
    else:
        form = CrearTrader()
    traders = Trader.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'trader.html', {'form': form, 'traders': traders})

    #traders = Trader.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    #return render(request, 'trader.html', {'traders':traders})



@login_required(login_url="login_view")
def sistema(request):
    if request.method =='POST':
        form = CrearSistema(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.fecha = timezone.now()
            instance.save()
            return redirect('sistema')
    else:
        form = CrearSistema()
    sistemas = Sistema.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'sistema.html', {'form': form, 'sistemas': sistemas})

@login_required(login_url="login_view")
def perfil(request):
    notificaciones = Notification.objects.filter()
    if request.method =='POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save();
            return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form})
    else:
        form = EditProfileForm(instance=request.user)
        return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form})

@login_required(login_url="login_view")
def password(request):
    notificaciones = Notification.objects.filter()
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save();
            update_session_auth_hash(request,form.user)
            return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form})
        else:
            return render(request,"password.html", {'notificaciones':notificaciones, 'form':form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,"password.html", {'notificaciones':notificaciones, 'form':form})

def password_reset(request):
        return render(request,"password_reset.html")

def password_reset_confirm(request):
        return render(request,"password_reset_confirm.html")        


@login_required(login_url="login_view")
def simple_upload(request):
    if request.method == 'POST':
        book_resource = resources.modelresource_factory(model=Book)()
        dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
        result = book_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
           result = book_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')
