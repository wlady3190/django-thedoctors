from django.db import models
from doctors.models import Doctor
from patients.models import Patient

from django.core.validators import MinValueValidator


from django.core.validators import MinValueValidator
from datetime import date


# ACEPTAR SOLO DECIMALES POSITIVOS

class PositiveDecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [MinValueValidator(0)]
        super().__init__(*args, **kwargs)


# SIGNOS VITALES
class Vital_Signs (models.Model):
    blood_pressure = models.CharField(
        max_length=7, verbose_name='presion_arterial', default=0, blank=True)
    heart_rate = models.PositiveSmallIntegerField(
        default=0,  verbose_name='frecuencia_cardiaca', blank=True)
    temperature = PositiveDecimalField(default=0.0, verbose_name='temperatura', decimal_places=1, max_digits=3, blank=True)
    breathing_frequency = models.PositiveSmallIntegerField(
        default=0, verbose_name='frecuencia_respiratoria', blank=True)
    oxygen_saturation = models.PositiveSmallIntegerField(
        default=0, verbose_name='saturacion_oxigeno', blank=True)

    class Meta:
        verbose_name = 'Vital_sign'
        verbose_name_plural = 'Vital_signs'


# DIAGNOSTICO

class Diagnosis(models.Model):
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
    diagnosis_type = models.CharField(
        choices=DIAGNOSIS_TYPE, verbose_name='diagnostico_tipo', max_length=25, blank=True)
    cie10_code = models.CharField(
        max_length=6, verbose_name='codigo_cie_10_odontologico', blank=True)
    description = models.TextField(verbose_name='diagnostico_descripcion', blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    class Meta:
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'

    def __str__(self):
        return self.description

# TRATAMIENTOS

class Treatment(models.Model):
    diagnoses = models.TextField(verbose_name='diagnostico', blank=True)
    complications = models.TextField(verbose_name='complicaciones', blank=True)
    procedures = models.TextField(verbose_name='procedimientos', blank=True)
    prescriptions = models.TextField(verbose_name='prescripciones', blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    class Meta:
        # ordering = ['diagnoses']
        verbose_name = 'Treatment'
        verbose_name_plural = 'Treatments'

    def __str__(self):
        return self.diagnoses


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, verbose_name='doctor_cita')
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, verbose_name='paciente_cita')
    vital_signs = models.OneToOneField(Vital_Signs, on_delete=models.CASCADE, default=0,  null=True)
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, verbose_name='diagnostico_cita')
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, verbose_name='tratamiento_cita')
    appointment_date_generated = models.DateField(verbose_name='fecha_cita_medica', default=date.today)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    class Meta:
        # ordering = ['patient, created']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return self.patient
