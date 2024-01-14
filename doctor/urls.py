from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('list',DoctorView)
router.register('specialization',SpecializationView)
router.register('designation',DesignationView)
router.register('available_time',AvailableTimeView)
router.register('review',ReviewView)

urlpatterns = [
    path('',include(router.urls))
]
