# Generated by Django 5.0.3 on 2024-04-19 14:53

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=45678, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, default='example@email.com', max_length=254, verbose_name='correo_paciente'),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='nombres'),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(blank=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthDate',
            field=models.DateField(default=datetime.date.today, verbose_name='fecha_nacimiento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='identification',
            field=models.TextField(blank=True, max_length=10, unique=True, verbose_name='cedula_identidad'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('MASCULINE', 'masculino'), ('FEMENINE', 'femenino')], default='', max_length=12, verbose_name='sexo'),
        ),
        migrations.CreateModel(
            name='Medical_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.TextField(blank=True, verbose_name='alergias')),
                ('diseases', models.TextField(blank=True, verbose_name='enfermedades_preexistentes')),
                ('medicines', models.TextField(blank=True, verbose_name='medicinas_actuales')),
                ('additional_info', models.TextField(blank=True, verbose_name='observaciones_adicionales')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'verbose_name': 'Medical_history',
                'verbose_name_plural': 'Medical_histories',
            },
        ),
        migrations.DeleteModel(
            name='Medical_Historial',
        ),
    ]
