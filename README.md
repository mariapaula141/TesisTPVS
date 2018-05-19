# TesisTPVS
Tesis Javeriana

Para correr esta aplicación de forma local se sebe installar:

[Python](https://www.python.org/downloads/).

Instalar un [entorno virtual](https://tutorial.djangogirls.org/es/django_installation/).
```
>>python3 -m venv myvenv
>>mkdir myenv
>>cd myenv
>>virtualenv .
>>myenv\Scripts\activate
>>cd..
```
Django
```
>>pip install django==2.0.3
```
Herramientas para unir Django con MySQL
```
>>pip install cymysql
>>pip install django-cymysql
```
MySQLClient
```
>>pip install mysqlclient
```
Crear un usuario para su correcto ingreso a la plataforma, dentro de la carpeta src del proyecto:
```
>>python manage.py createsuperuser
```
Cambiar los datos de la base de datos a los propios:
1. En el Archivo `settings.py` en `mysite`, cambiar el apartado DATABASE

Migrar el modelo a la base de datos, dentro de la carpeta src del proyecto:
```
>>python manage.py makemigrations
>>python manage.py showmigrations
>>python manage.py migrate
```
Por último se debe correr el servidor 
```
>>python manage.py runserver
```
E ingresar a:
http://localhost:8000/login

