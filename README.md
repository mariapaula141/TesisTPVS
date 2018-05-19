# TesisTPVS
Tesis Javeriana

Una vez descargue el proyecto correr esta aplicación de forma local se sebe installar:


[Python](https://www.python.org/downloads/).

Acceder al [entorno virtual](https://tutorial.djangogirls.org/es/django_installation/) y activarlo .
```
>> cd ENV
>>source bin/activate
>>cd ..
```
  En caso tal que quiera realizar su propio entorno virtual, el proceso a seguir es:
  ```
  sudo pip install virtualenv
  pip install django-import-export
  pip install djangorestframework
  pip install django-notifications-hq
  pip install cymysql
  sudo apt-get install mysql-server
  pip install django mysqlclient
  pip install django-alert
  pip install django-webline-notifications
  pip install virtualenvwrapper
  pip install python-crontab
  ```

Crear un usuario para su correcto ingreso a la plataforma, dentro de la carpeta src del proyecto:
```
>>python manage.py createsuperuser
```
En caso de cambios en la base de datos usted deberá migrar el modelo a la base de datos, dentro de la carpeta src del proyecto:
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

