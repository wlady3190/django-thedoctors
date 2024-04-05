from django.db import models

# Create your models here.

# class Allergy(models.Model):
#     nameAllergy = models.CharField()
#     descriptionAllergiy = models.TextField()


# class Diseases(models.Model):
#     nameDisease = models.CharField()
#     descriptionDisease = models.TextField()


class Patient (models.Model):

    SEX_CHOICES = [
        ('MASCULINE', "masculino"),
        ('FEMENINE', "femenino")
    ]
    name = models.CharField(max_length=150, verbose_name="nombres")
    lastName = models.CharField(max_length=150, verbose_name="apellidos")
    birthDate = models.DateField(verbose_name="fecha_nacimiento")
    identification = models.TextField(
        max_length=10, verbose_name="cedula_identidad")
    address = models.TextField(verbose_name="direccion")
    phone = models.CharField(max_length=15, verbose_name='telefono')
    sex = models.CharField(max_length=12, choices=SEX_CHOICES,
                           default="", verbose_name="sexo")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="fecha_actualizacion")

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['lastName']


class Medical_Historial(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    allergy = models.TextField(verbose_name="alergias")
    diseases = models.TextField(verbose_name="enfermedades_preexistentes")
    medicines = models.TextField(verbose_name="medicinas_actuales")
    pregnant = models.BooleanField(verbose_name="embarazo")
    
    
    def __str__(self) :
        return self.patient
    
    class Meta:
        verbose_name = 'Medical_historial'
        verbose_name_plural = 'Medical_historials'
