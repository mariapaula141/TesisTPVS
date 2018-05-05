from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    accion = models.CharField(max_length=200)

    def update(self):
        self.fecha = timezone.now()
        self.save()
    def __str__(self):
        return self.accion

@receiver(post_save, sender=Archivo)
def archivo_nuevo(sender, instance,created, **kwargs):
        Accion.objects.create(accion='creao un archivo', author_id=instance.author_id)

    # This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Dimcontraparte(models.Model):
    idcontraparte = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dimcontraparte'


class Dimestado(models.Model):
    idestado = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dimestado'


class Dimfecha(models.Model):
    idfecha = models.CharField(primary_key=True, max_length=50)
    anio = models.CharField(max_length=20, blank=True, null=True)
    mes = models.CharField(max_length=20, blank=True, null=True)
    dia = models.CharField(max_length=20, blank=True, null=True)
    nombre_mes = models.CharField(max_length=20, blank=True, null=True)
    nombre_dia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dimfecha'


class Diminfomoneda(models.Model):
    idmoneda = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'diminfomoneda'


class Dimportafolio(models.Model):
    idportafolio = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dimportafolio'


class Dimproducto(models.Model):
    idproducto = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    tipo_operacion = models.CharField(max_length=20)

    class Meta:
        db_table = 'dimproducto'


class Dimsistema(models.Model):
    idsistema = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=500)

    class Meta:
        db_table = 'dimsistema'


class Dimtrader(models.Model):
    idtrader = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'dimtrader'

class Operaciones(models.Model):
    idoperacion = models.CharField(db_column='idOperacion', primary_key=True, max_length=20)  # Field name made lowercase.
    contrapartecierre = models.CharField(db_column='contraparteCierre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idestado = models.CharField(db_column='idEstado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechacarga = models.CharField(db_column='fechaCarga', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechafinalizacion = models.CharField(db_column='fechaFinalizacion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechainsercion = models.CharField(db_column='fechaInsercion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechapago = models.CharField(db_column='fechaPago', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idmonedafuerte = models.CharField(db_column='idMonedaFuerte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idmonedadebil = models.CharField(db_column='idMonedaDebil', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idportafolio = models.CharField(db_column='idPortafolio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.CharField(db_column='idProducto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idsistema = models.CharField(db_column='idSistema', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idtrader = models.CharField(db_column='idTrader', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cant_contratos = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'operaciones'
