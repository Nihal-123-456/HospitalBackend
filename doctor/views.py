from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters, pagination
# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 
    page_size_query_param = page_size
    max_page_size = 100

class DoctorView(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

class SpecializationView(viewsets.ModelViewSet):
    queryset = SpecializationModel.objects.all()
    serializer_class = SpecializationSerializer

class DesignationView(viewsets.ModelViewSet):
    queryset = DesignationModel.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeForEachDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctormodel = doctor_id)
        return query_set

class AvailableTimeView(viewsets.ModelViewSet):
    queryset = AvailableTimeModel.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForEachDoctor]

class ReviewView(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer