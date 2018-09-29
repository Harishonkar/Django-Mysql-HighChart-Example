from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin
from .models import data

@admin.register(data)
class PersonAdmin(ImportExportModelAdmin):
    pass