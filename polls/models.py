from django.db import models
from django.utils import timezone

class Sistema(models.Model):
    identificador = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    descripcion =  models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = models.DateTimeField( blank=True, null=True)


    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Trader(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    fecha = models.DateTimeField( blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.username

class Portafolio(models.Model):
    identificador = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField( blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Archivo(models.Model):
    ruta = models.FileField()
    fecha = models.DateTimeField( blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def update(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.ruta
