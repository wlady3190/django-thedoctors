from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from PIL import  Image
# Create your models here.

class Custom_User(AbstractBaseUser):
    identifier = models.EmailField(unique=True, max_length=40, default='example@example.com')
    USERNAME_FIELD = 'identifier'

class Doctor (models.Model):
    user = models.OneToOneField(
        Custom_User, on_delete=models.CASCADE, verbose_name='usuario_doctor')
    #email = models.EmailField(unique=True, verbose_name='correo_doctor')
    name = models.CharField(max_length=150, verbose_name="nombres_doctor")
    lastName = models.CharField(max_length=150, verbose_name="apellidos_doctor")
    birthDate = models.DateField(verbose_name="fecha_nacimiento_doctor")
    identification = models.TextField(
        max_length=10, unique=True, verbose_name="cedula_identidad_doctor")
    registryCode = models.CharField(
        max_length=20, verbose_name="codigo_registro_doctor")
    address = models.TextField(verbose_name="direccion_doctor")
    phone = models.CharField(max_length=15, verbose_name='telefono_doctor')
    photo = models.ImageField(default='profile.png',
                              upload_to='user_profile')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion_doctor")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion_doctor")

    def __str__(self):
        return f'{self.user} Profile'

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['lastName']


    #Ajustar tamaño de la imagen creada para que no sea muy grande

    def save(self, *args, **kwargs):
        #super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height> 300 or img.width > 300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
