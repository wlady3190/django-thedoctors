# Generated by Django 5.0.3 on 2024-04-14 18:56

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctors'},
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='nombres_doctor'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='apellido_doctor'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='direccion_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='birthDate',
            field=models.DateField(default=datetime.date.today, verbose_name='fecha_nacimiento_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha_creacion_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='identification',
            field=models.CharField(blank=True, max_length=15, verbose_name='cedula_identidad_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefono_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, default='profile.png', upload_to='user_profile'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='registryCode',
            field=models.CharField(blank=True, max_length=20, verbose_name='codigo_registro_doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha_actualizacion_doctor'),
        ),
    ]