from django.db import models
from patient.models import *
from doctor.models import *

# Create your models here.
APPOINTMENT_TYPE={
    ('Online','Online'),
    ('Offline','Offline'),
}
APPOINTMENT_STATUS={
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
}

class AppointmentModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPE, max_length=15)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=15, default='Pending')
    symptoms = models.TextField()
    time = models.ForeignKey(AvailableTimeModel, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
