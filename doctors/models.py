from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.db.models.signals import post_save
from PIL import Image
from django.dispatch import receiver


# Regex para validar campos



class Doctor (models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default= None )
    first_name = models.CharField(max_length=50, verbose_name='nombres_doctor', blank=True)
    last_name = models.CharField(max_length=50, verbose_name='apellido_doctor', blank=True)
    birthDate = models.DateField(verbose_name="fecha_nacimiento_doctor", default=date.today)
    identification = models.CharField(
        max_length=15, verbose_name="cedula_identidad_doctor", blank=True)
    registryCode = models.CharField(
        max_length=20, verbose_name="codigo_registro_doctor", blank=True)
    address = models.CharField(verbose_name="direccion_doctor", max_length=200, blank=True)
    phone = models.CharField(max_length=15, verbose_name='telefono_doctor', blank=True)
    photo = models.ImageField(default='profile.png',
                              upload_to='user_profile', blank=True)
    specialty = models.CharField(max_length=50, verbose_name='especialidad')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion_doctor")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion_doctor")


# a partir de esto se crea lo signasl para la creación correcta de perfiles

    def __str__(self):
        return f'{self.user} Doctor'

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    # Ajustar tamaño de la imagen creada para que no sea muy grande

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
            

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.doctor.save()