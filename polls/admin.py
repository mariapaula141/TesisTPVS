from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from import_export import resources
from .models import Mensaje

admin.site.register(Mensaje)
