from django.db import models
from django.contrib.auth.models import User
from patient.models import *

# Create your models here.
class SpecializationModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.name

class DesignationModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.name

class AvailableTimeModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(DesignationModel)
    specialization = models.ManyToManyField(SpecializationModel)
    available_time = models.ManyToManyField(AvailableTimeModel)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username

STAR_CHOICE = {
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
}

class ReviewModel(models.Model):
    reviewer = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICE, max_length=20)