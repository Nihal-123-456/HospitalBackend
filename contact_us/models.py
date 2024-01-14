from django.db import models

# Create your models here.
class ContactUsModel(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'