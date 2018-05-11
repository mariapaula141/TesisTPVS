from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Archivo(models.Model):
    ruta = models.FileField()
    fecha = models.DateTimeField( blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def update(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.ruta

class Mensaje(models.Model):
    fecha = models.DateTimeField( blank=True, null=True)
    mensaje = models.CharField(max_length=200)

    def update(self):
        self.fecha = timezone.now()
        self.save()
    def __str__(self):
        return self.mensaje

class Accion(models.Model):
    fecha = models.DateTimeField( blank=True, null=True)
    author = models.CharField(max_length=200)
    accion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)

    def update(self):
        self.fecha = timezone.now()
        self.save()





# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dimcontraparte(models.Model):
    idcontraparte = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'dimcontraparte'


class Dimestado(models.Model):
    idestado = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'dimestado'


class Dimfecha(models.Model):
    idfecha = models.CharField(db_column='idFecha', primary_key=True, max_length=50)  # Field name made lowercase.
    anio = models.SmallIntegerField()
    mes = models.SmallIntegerField()
    nombre_mes = models.CharField(db_column='nombre_Mes', max_length=50)  # Field name made lowercase.
    dia = models.SmallIntegerField()
    nombre_dia = models.CharField(db_column='nombre_Dia', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'dimfecha'


class Diminfomoneda(models.Model):
    idmoneda = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'diminfomoneda'


class Dimportafolio(models.Model):
    idportafolio = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'dimportafolio'


class Dimproducto(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipo_operacion = models.CharField(max_length=50)

    class Meta:
        db_table = 'dimproducto'


class Dimsistema(models.Model):
    idsistema = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=500)

    class Meta:
        db_table = 'dimsistema'


class Dimtrader(models.Model):
    idtrader = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'dimtrader'

'''
class Factoperacion(models.Model):
    idoperacion = models.CharField(db_column='idOperacion', primary_key=True, max_length=50)  # Field name made lowercase.
    contraparte = models.CharField(max_length=50, blank=True, null=True)
    idestado = models.CharField(db_column='idEstado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_carga = models.CharField(max_length=50, blank=True, null=True)
    fecha_finalizacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_insercion = models.CharField(max_length=50, blank=True, null=True)
    fecha_pago = models.CharField(max_length=50, blank=True, null=True)
    idmonedafuerte = models.CharField(db_column='idMonedaFuerte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idmonedadebil = models.CharField(db_column='idMonedaDebil', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idportafolio = models.CharField(db_column='idPortafolio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.CharField(db_column='idProducto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idsistema = models.CharField(db_column='idSistema', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idtrader = models.CharField(db_column='idTrader', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cant_contratos = models.IntegerField(blank=True, null=True)
    monto_operacion = models.FloatField(blank=True, null=True)
    precio_cambio_par = models.FloatField(blank=True, null=True)
    p_l = models.FloatField(db_column='p_L', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'factoperacion'
        '''
