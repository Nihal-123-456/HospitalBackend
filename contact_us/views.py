from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer
