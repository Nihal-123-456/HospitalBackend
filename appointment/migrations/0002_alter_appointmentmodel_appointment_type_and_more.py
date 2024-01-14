# Generated by Django 4.2.4 on 2024-01-11 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_reviewmodel_rating'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentmodel',
            name='appointment_type',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=15),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletimemodel'),
        ),
    ]