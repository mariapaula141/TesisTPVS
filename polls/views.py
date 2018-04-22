from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Trader, Portafolio, Archivo, Sistema, Mensaje
from .forms import CargarArchivo, CrearTrader, CrearPortafolio, CrearSistema, RegistrationForm
from django.utils import timezone
import tablib
from import_export import resources
from rest_framework import viewsets
from .serializers import MensajeSerializer
# Create your views here.


from django.http import HttpResponse

#API
class MensajeView(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer

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



#Index
@login_required(login_url="login")
def index(request):
    return render(request,"index.html")


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
@login_required(login_url="login")
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

@login_required(login_url="login")
def contraparte(request):
    return render(request,"contraparte.html")

@login_required(login_url="login")
def estado(request):
    return render(request,"estado.html")

@login_required(login_url="login")
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


@login_required(login_url="login")
def producto(request):
    return render(request,"producto.html")

@login_required(login_url="login")
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



@login_required(login_url="login")
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



def simple_upload(request):
    if request.method == 'POST':
        book_resource = resources.modelresource_factory(model=Book)()
        dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
        result = book_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
           result = book_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')
