from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.conf import settings
from .models import *
from .forms import *
from django.utils import timezone
from rest_framework import viewsets
from .serializers import MensajeSerializer
from webline_notifications.models import Notification

import os
import subprocess


from wsgiref.util import FileWrapper


# Create your views here.


from django.http import HttpResponse

#API
class MensajeView(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    #falta guardar esto en el la base de datos

#Registro
@login_required(login_url="login_view")
def register(request):
    usuario = request.user
    if usuario.is_staff:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'El usuario se ha guardado con exito')
            else:
                messages.error(request, 'El usuario no se ha guardado, por favor verifique los datos ingresados')
        else:
            form = RegistrationForm()
        return render(request,'register.html',{'form':form,'usuario':usuario})
    else:
        return render(request,'permiso.html',{'usuario':usuario})




#Espera
def permiso(request):
    return render(request,"permiso.html")

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

def manual(request):
    try:
        f = open(os.path.join(settings.MEDIA_ROOT,'Manual.pdf'), "r")
        response = HttpResponse(FileWrapper(f), content_type='application/pdf')
        response ['Content-Disposition'] = 'attachment; filename=resume.pdf'
        f.close()
        return response

    except FileNotFoundError:
        raise Http404()

#Logs
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'El usuario o contraseña no concuerdan')
    else:
        form = AuthenticationForm()
    return render(request,'login_view.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_view')

#post_save



#Menu
@login_required(login_url="login_view")
def archivo(request):
    if request.method =='POST':
        form = CargarArchivo(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance.ruta)
            if instance.ruta=="Spot-fwd.csv" or instance.ruta=="CURR_FUT.csv":
                instance.author = request.user
                instance.fecha = timezone.now()
                instance.save(using='default')
                messages.success(request, 'Guardado con exito')
                if instance.ruta=="Spot-fwd.csv":
                	Accion.objects.using('default').create(accion='creando un archivo Spot-fwdx.csv', author=request.user.get_username(), estado='Cargado', fecha= timezone.now())
                	subprocess.Popen(["bash", "/home/TPVS/TesisTPVS/Jobs/ETL_Spot/ETL_Spot/ETL_Spot_run.sh"])
                else:
                	Accion.objects.using('default').create(accion='creando un archivo CURR_FUT.csv', author=request.user.get_username(), estado='Cargado', fecha= timezone.now())
                	subprocess.Popen(["bash", "/home/TPVS/TesisTPVS/Jobs/ETL_Futuros/ETL_Fut/ETL_Fut_run.sh"])
            else:
                messages.error(request, 'El archivo ingresado no cuenta con el formato adecuado')
        #    return redirect('archivo')
    else:
        form = CargarArchivo()
    registros = Accion.objects.using('default')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request,"archivo.html",{'form':form, 'registros':registros,'notificaciones':notificaciones, 'usuario':usuario})


@login_required(login_url="login_view")
def producto(request):
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request,"producto.html",{'notificaciones':notificaciones, 'usuario':usuario})
'''
@login_required(login_url="login_view")
def parMoneda(request):
    return render(request,"pares.html")

@login_required(login_url="login_view")
def info(request):
    return render(request,"info.html")
'''
@login_required(login_url="login")
def contraparte(request):
    if request.method =='POST':
        form = CrearContraparte(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='datamart')
            Dimcontraparte.objects.using('default').filter(idcontraparte=form.instance.idcontraparte).delete()
            messages.success(request, 'Se ha añadido el registro al datamart con exito')
        else:
            messages.error(request, 'El formato no es válido')
    else:
        form = CrearContraparte()
    contraparteStage = Dimcontraparte.objects.using('default').order_by('idcontraparte')
    contraparteDatamart = Dimcontraparte.objects.using('datamart').order_by('idcontraparte')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request,'contraparte.html',{'form':form,'contraparteStage':contraparteStage, 'contraparteDatamart':contraparteDatamart,'notificaciones':notificaciones, 'usuario':usuario})



@login_required(login_url="login_view")
def estado(request):
    if request.method =='POST':
        form = CrearEstado(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='datamart')
            Dimestado.objects.using('default').filter(idestado=form.instance.idestado).delete()
            messages.success(request, 'Se ha añadido el registro al datamart con exito')
        else:
            messages.error(request, 'El formato no es válido')
    else:
        form = CrearEstado()
    estadoStage = Dimestado.objects.using('default').order_by('idestado')
    estadoDatamart = Dimestado.objects.using('datamart').order_by('idestado')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request, 'estado.html', {'form':form,'estadoStage':estadoStage, 'estadoDatamart':estadoDatamart,'notificaciones':notificaciones, 'usuario':usuario})

@login_required(login_url="login_view")
def portafolio(request):
    if request.method =='POST':
        form = CrearPortafolio(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='datamart')
            Dimportafolio.objects.using('default').filter(idportafolio=form.instance.idportafolio).delete()
            messages.success(request, 'Se ha añadido el registro al datamart con exito')
        else:
            messages.error(request, 'El formato no es válido')
    else:
        form = CrearPortafolio()
    portafolioStage = Dimportafolio.objects.using('default').order_by('idportafolio')
    portafolioDatamart = Dimportafolio.objects.using('datamart').order_by('idportafolio')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request, 'portafolio.html', {'form':form,'portafolioStage':portafolioStage, 'portafolioDatamart':portafolioDatamart,'notificaciones':notificaciones, 'usuario':usuario})

@login_required(login_url="login")
def sistema(request):
    if request.method =='POST':
        form = CrearSistema(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='datamart')
            Dimsistema.objects.using('default').filter(idsistema=form.instance.idsistema).delete()
            messages.success(request, 'Se ha añadido el registro al datamart con exito')
        else:
            messages.error(request, 'El formato no es válido')

    else:
        form = CrearSistema()
    sistemaStage = Dimsistema.objects.using('default').order_by('idsistema')
    sistemaDatamart = Dimsistema.objects.using('datamart').order_by('idsistema')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request,'sistema.html',{'form':form,'sistemaStage':sistemaStage, 'sistemaDatamart':sistemaDatamart, 'notificaciones':notificaciones, 'usuario':usuario})


@login_required(login_url="login_view")
def trader(request):
    if request.method =='POST':
        form = CrearTrader(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using='datamart')
            Dimtrader.objects.using('default').filter(idtrader=form.instance.idtrader).delete()
            messages.success(request, 'Se ha añadido el registro al datamart con exito')
        else:
            messages.error(request, 'El formato no es válido')
    else:
        form = CrearTrader()
    tradersStage = Dimtrader.objects.using('default').order_by('idtrader')
    tradersDatamart = Dimtrader.objects.using('datamart').order_by('idtrader')
    usuario = request.user
    notificaciones = Notification.objects.filter()
    return render(request, 'trader.html', {'form':form,'tradersStage':tradersStage, 'tradersDatamart':tradersDatamart, 'notificaciones':notificaciones, 'usuario':usuario})
    #return render(request, 'trader.html', {'traders':traders})

@login_required(login_url="login_view")
def perfil(request):
    notificaciones = Notification.objects.filter()
    usuario = request.user
    if request.method =='POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se han actualizado sus datos con exito')
            return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form, 'usuario':usuario})
        else:
            messages.error(request, 'El formato no es válido')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form, 'usuario':usuario})

@login_required(login_url="login_view")
def password(request):
    notificaciones = Notification.objects.filter()
    usuario = request.user
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return render(request,"perfil.html", {'notificaciones':notificaciones, 'form':form, 'usuario':usuario})
        else:
            return render(request,"password.html", {'notificaciones':notificaciones, 'form':form, 'usuario':usuario})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,"password.html", {'notificaciones':notificaciones, 'form':form, 'usuario':usuario})

def password_reset(request):
        return render(request,"password_reset.html")

def password_reset_confirm(request):
        return render(request,"password_reset_confirm.html")
