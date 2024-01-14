from django.contrib import admin
from .models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','description']

admin.site.register(ServiceModel,ServiceAdmin)