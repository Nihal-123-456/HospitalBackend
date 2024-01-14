from django.contrib import admin
from .models import *

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_name','phone']

    def patient_name(self,obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
admin.site.register(PatientModel,PatientAdmin)