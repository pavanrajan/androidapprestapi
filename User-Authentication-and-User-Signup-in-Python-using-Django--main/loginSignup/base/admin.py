from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AndroidApp

@admin.register(AndroidApp)
class AndroidAppAdmin(admin.ModelAdmin):
    list_display = ("name", "package_name")
