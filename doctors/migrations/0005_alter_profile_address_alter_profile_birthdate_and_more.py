# Generated by Django 5.0.3 on 2024-04-10 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_rename_first_names_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='direccion_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='fecha_nacimiento_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='nombres_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.CharField(blank=True, max_length=15, verbose_name='cedula_identidad_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='apellido_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefono_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profile.png', upload_to='user_profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='registryCode',
            field=models.CharField(blank=True, max_length=20, verbose_name='codigo_registro_doctor'),
        ),
    ]