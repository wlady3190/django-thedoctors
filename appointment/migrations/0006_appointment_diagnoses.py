# Generated by Django 5.0.3 on 2024-04-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointment_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='diagnoses',
            field=models.TextField(blank=True, verbose_name='Diagnóstico'),
        ),
    ]