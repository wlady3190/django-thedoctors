# Generated by Django 5.0.3 on 2024-04-04 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombres')),
                ('lastName', models.CharField(max_length=150, verbose_name='apellidos')),
                ('birthDate', models.DateField(verbose_name='fecha_nacimiento')),
                ('identification', models.TextField(max_length=10, verbose_name='cedula_identidad')),
                ('address', models.TextField(verbose_name='direccion')),
                ('phone', models.CharField(max_length=15, verbose_name='telefono')),
                ('sex', models.CharField(choices=[('MASCULINE', 'masculino'), ('FEMENINE', 'femenino')], default='', max_length=12, verbose_name='sexo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
                'ordering': ['lastName'],
            },
        ),
        migrations.CreateModel(
            name='Medical_Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.TextField(verbose_name='alergias')),
                ('diseases', models.TextField(verbose_name='enfermedades_preexistentes')),
                ('medicines', models.TextField(verbose_name='medicinas_actuales')),
                ('pregnant', models.BooleanField(verbose_name='embarazo')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'verbose_name': 'Medical_historial',
                'verbose_name_plural': 'Medical_historials',
            },
        ),
    ]
