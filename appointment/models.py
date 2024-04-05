from django.db import models
from doctors.models import Doctor
from patients.models import Patient

from django.core.validators import MinValueValidator


from django.core.validators import MinValueValidator


# ACEPTAR SOLO DECIMALES POSITIVOS

class PositiveDecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [MinValueValidator(0)]
        super().__init__(*args, **kwargs)

# SIGNOS VITALES


class Vital_sign (models.Model):
    blood_pressure = models.CharField(
        max_length=7, verbose_name='presion_arterial')
    heart_rate = models.PositiveSmallIntegerField(
        default=0,  verbose_name='frecuencia_cardiaca')
    temperature = PositiveDecimalField(default=0.0, verbose_name='temperatura', decimal_places=1, max_digits=3)
    breathing_frequency = models.PositiveSmallIntegerField(
        default=0, verbose_name='frecuencia_respiratoria')
    oxygen_saturation = models.PositiveSmallIntegerField(
        default=0, verbose_name='saturacion_oxigeno')

    class Meta:
        verbose_name = 'Vital_sign'
        verbose_name_plural = 'Vital_signs'


# DIAGNOSTICO

class Diagnosis(models.Model):
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
    diagnosis_type = models.CharField(
        choices=DIAGNOSIS_TYPE, verbose_name='diagnostico_tipo')
    cie10_code = models.CharField(
        max_length=4, verbose_name='codigo_cie_10_odontologico')
    description = models.TextField(verbose_name='diagnostico_descripcion')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    class Meta:
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnosiss'

    def __str__(self):
        return self.description


# TRATAMIENTOS

class Treatment(models.Model):
    diagnoses = models.TextField(verbose_name='diagnostico')
    complications = models.TextField(verbose_name='complicaciones')
    procedures = models.TextField(verbose_name='procedimientos')
    prescriptions = models.TextField(verbose_name='prescripciones')
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
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name='paciente_cita')
    vital_signs = models.OneToOneField(Vital_sign, on_delete=models.CASCADE, verbose_name='signos_vitales')
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, verbose_name='diagnostico_cita')
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, verbose_name='tratamiento_cita')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    class Meta:
        # ordering = ['patient, created']
        verbose_name = 'Treatment'
        verbose_name_plural = 'Treatments'

    def __str__(self):
        return self.patient
