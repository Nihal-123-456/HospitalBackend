# Generated by Django 4.2.4 on 2024-01-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='rating',
            field=models.CharField(choices=[('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐', '⭐'), ('⭐⭐⭐', '⭐⭐⭐')], max_length=20),
        ),
    ]
