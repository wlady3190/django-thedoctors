from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient (models.Model):

    SEX_CHOICES = [
        ('MASCULINE', "masculino"),
        ('FEMENINE', "femenino")
    ]
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, verbose_name="nombres", blank=True)
    last_name = models.CharField(max_length=150, verbose_name="apellidos", blank=True)
    birthDate = models.DateField(verbose_name="fecha_nacimiento", default= date.today)
    identification = models.TextField(
        max_length=10, unique=True, verbose_name="cedula_identidad", blank=True)
    address = models.TextField(verbose_name="direccion", blank=True)
    email= models.EmailField(verbose_name='correo_paciente', default='example@email.com' , blank=True)
    phone = models.CharField(max_length=15, verbose_name='telefono', blank=True)
    sex = models.CharField(max_length=12, choices=SEX_CHOICES,
                           default="", verbose_name="sexo", blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Medical_History(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    allergy = models.TextField(verbose_name="alergias", blank=True)
    diseases = models.TextField(verbose_name="enfermedades_preexistentes", blank=True)
    medicines = models.TextField(verbose_name="medicinas_actuales", blank=True)
    additional_info = models.TextField(verbose_name="observaciones_adicionales", blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")
    
    
    def __str__(self):
        return f"Medical History for {self.patient.first_name} {self.patient.last_name}"

    class Meta:
        verbose_name = 'Medical_history'
        verbose_name_plural = 'Medical_histories'
