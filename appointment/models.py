from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


from django.core.validators import MinValueValidator
from datetime import date


# ACEPTAR SOLO DECIMALES POSITIVOS

class PositiveDecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [MinValueValidator(0)]
        super().__init__(*args, **kwargs)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    appointment_date_generated = models.DateField(verbose_name='fecha_cita_medica', default=date.today)
    # !Signos vitales
    blood_pressure = models.CharField(
        max_length=7, verbose_name='presion_arterial', default=0, blank=True)
    heart_rate = models.PositiveSmallIntegerField(
        default=0,  verbose_name='frecuencia_cardiaca', blank=True)
    temperature = PositiveDecimalField(default=0.0, verbose_name='temperatura', decimal_places=1, max_digits=3, blank=True)
    breathing_frequency = models.PositiveSmallIntegerField(
        default=0, verbose_name='frecuencia_respiratoria', blank=True)
    oxygen_saturation = models.PositiveSmallIntegerField(
        default=0, verbose_name='saturacion_oxigeno', blank=True)

    # ! Diagnóstico
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
   
    diagnosis_type = models.CharField(
        choices=DIAGNOSIS_TYPE, verbose_name='diagnostico_tipo', max_length=25, blank=True)
    cie10_code = models.CharField(
        max_length=6, verbose_name='codigo_cie_10_odontologico', blank=True)
    diagnoses = models.TextField(blank=True, verbose_name='Diagnóstico')

    #! Complicaciones
    diagnoses_complications = models.TextField(verbose_name='diagnostico_complicaciones', blank=True)
    procedures = models.TextField(verbose_name='procedimientos', blank=True)
    prescriptions = models.TextField(verbose_name='prescripciones', blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")
    

    class Meta:
        # ordering = ['patient, created']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'Cita generada el dia {str(self.appointment_date_generated)}'

