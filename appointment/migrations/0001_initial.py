# Generated by Django 5.0.3 on 2024-04-04 23:47

import appointment.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_type', models.CharField(choices=[('PRE', 'presuntivo'), ('DEF', 'definitivo')], verbose_name='diagnostico_tipo')),
                ('cie10_code', models.CharField(max_length=4, verbose_name='codigo_cie_10_odontologico')),
                ('description', models.TextField(verbose_name='diagnostico_descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')),
            ],
            options={
                'verbose_name': 'Diagnosis',
                'verbose_name_plural': 'Diagnosiss',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnoses', models.TextField(verbose_name='diagnostico')),
                ('complications', models.TextField(verbose_name='complicaciones')),
                ('procedures', models.TextField(verbose_name='procedimientos')),
                ('prescriptions', models.TextField(verbose_name='prescripciones')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')),
            ],
            options={
                'verbose_name': 'Treatment',
                'verbose_name_plural': 'Treatments',
            },
        ),
        migrations.CreateModel(
            name='Vital_sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_pressure', models.CharField(max_length=7, verbose_name='presion_arterial')),
                ('heart_rate', models.PositiveSmallIntegerField(default=0, verbose_name='frecuencia_cardiaca')),
                ('temperature', appointment.models.PositiveDecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='temperatura')),
                ('breathing_frequency', models.PositiveSmallIntegerField(default=0, verbose_name='frecuencia_respiratoria')),
                ('oxygen_saturation', models.PositiveSmallIntegerField(default=0, verbose_name='saturacion_oxigeno')),
            ],
            options={
                'verbose_name': 'Vital_sign',
                'verbose_name_plural': 'Vital_signs',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='doctor_cita')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='paciente_cita')),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.diagnosis', verbose_name='diagnostico_cita')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.treatment', verbose_name='tratamiento_cita')),
            ],
            options={
                'verbose_name': 'Treatment',
                'verbose_name_plural': 'Treatments',
            },
        ),
    ]
