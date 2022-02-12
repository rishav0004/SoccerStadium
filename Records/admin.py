from django.contrib import admin
from .models import Players
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

@admin.register(Players)
class playerdata(ImportExportActionModelAdmin):
    pass
