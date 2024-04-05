from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='usuario')
    email = models.EmailField(unique=True, verbose_name='correo_doctor')
    name = models.CharField(max_length=150, verbose_name="nombres")
    lastName = models.CharField(max_length=150, verbose_name="apellidos")
    birthDate = models.DateField(verbose_name="fecha_nacimiento")
    identification = models.TextField(
        max_length=10, unique=True, verbose_name="cedula_identidad")
    registryCode = models.CharField(
        max_length=20, verbose_name="codigo_registro")
    address = models.TextField(verbose_name="direccion")
    phone = models.CharField(max_length=15, verbose_name='telefono')
    photo = models.ImageField(default='profile.png',
                              upload_to='user_profile')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['lastName']
    #Ajustat tamaño de la imagen creada
    
