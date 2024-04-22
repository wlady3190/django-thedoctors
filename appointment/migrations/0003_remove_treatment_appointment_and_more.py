# Generated by Django 5.0.3 on 2024-04-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_vital_signs_delete_vital_sign_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='vital_signs',
            name='appointment',
        ),
        migrations.AddField(
            model_name='appointment',
            name='blood_pressure',
            field=models.CharField(blank=True, default=0, max_length=7, verbose_name='presion_arterial'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='breathing_frequency',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='frecuencia_respiratoria'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='cie10_code',
            field=models.CharField(blank=True, max_length=6, verbose_name='codigo_cie_10_odontologico'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='complications',
            field=models.TextField(blank=True, verbose_name='complicaciones'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='diagnosis_type',
            field=models.CharField(blank=True, choices=[('PRE', 'presuntivo'), ('DEF', 'definitivo')], max_length=25, verbose_name='diagnostico_tipo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='heart_rate',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='frecuencia_cardiaca'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='oxygen_saturation',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='saturacion_oxigeno'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescriptions',
            field=models.TextField(blank=True, verbose_name='prescripciones'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='procedures',
            field=models.TextField(blank=True, verbose_name='procedimientos'),
        ),
        migrations.DeleteModel(
            name='Diagnosis',
        ),
        migrations.DeleteModel(
            name='Treatment',
        ),
        migrations.DeleteModel(
            name='Vital_Signs',
        ),
    ]