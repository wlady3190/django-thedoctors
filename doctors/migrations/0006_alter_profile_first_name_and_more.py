# Generated by Django 5.0.3 on 2024-04-11 02:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_profile_address_alter_profile_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z]*$', 'Ingresar solo letras')], verbose_name='nombres_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Ingresar solo números')], verbose_name='cedula_identidad_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z]*$', 'Ingresar solo letras')], verbose_name='apellido_doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Ingresar solo números')], verbose_name='telefono_doctor'),
        ),
    ]
