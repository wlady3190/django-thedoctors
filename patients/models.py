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
        ('MASCULINE', "Masculino"),
        ('FEMENINE', "Femenino")
    ]
    name = models.CharField(max_lenght=150, verbose_name="nombres")
    lastName = models.CharField(max_lenght=150, verbose_name="apellidos")
    birthDate = models.DateField(verbose_name="fecha_nacimiento")
    identification = models.TextField(
        max_lenght=10, verbose_name="cedula_identidad")
    address = models.TextField(verbose_name="Direccion")
    sex = models.CharField(max_lenght=12, choices=SEX_CHOICES,
                           default="", verbose_name="Sexo")
    allergy = models.TextField(verbose_name="Alergias")
    diseases = models.TextField(verbose_name="Enfermedades_preexistentes")
    medicines = models.TextField(verbose_name="Medicinas_actuales")
    pregnant = models.BooleanField(verbose_name="Embarazo")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha_creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha_actualizacion")

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['lastName']
