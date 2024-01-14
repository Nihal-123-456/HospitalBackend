from django.contrib import admin
from .models import *
# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}
    list_display = ['name','slug']

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}
    list_display = ['name','slug']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','fee','meet_link']

    def doctor_name(self,obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','body','created_on','rating']
    def patient_name(self,obj):
        return f'{obj.reviewer.user.first_name} {obj.reviewer.user.last_name}'
    def doctor_name(self,obj):
        return f'{obj.doctor.user.first_name} {obj.doctor.user.last_name}'

admin.site.register(SpecializationModel, SpecializationAdmin)
admin.site.register(DesignationModel, DesignationAdmin)
admin.site.register(AvailableTimeModel)
admin.site.register(DoctorModel,DoctorAdmin)
admin.site.register(ReviewModel,ReviewAdmin)