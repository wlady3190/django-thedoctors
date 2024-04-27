from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from datetime import time

# Create your models here.


class Patientimage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    front = models.ImageField(
        verbose_name="foto_frontal", default='patients_profile/front/default_image.jpeg',
        upload_to='patients_profile/front')
    front_smiling = models.ImageField(
        verbose_name="frontal_sonriendo", default='patients_profile/front_smiling/default_image.jpeg', upload_to='patients_profile/front_smiling')
    right_side = models.ImageField(
        verbose_name="lateral_derecha", default='patients_profile/rigth_side/default_image.jpeg', upload_to='patients_profile/rigth_side')
    right_side_smiling = models.ImageField(
        verbose_name="lateral_derecha_sonriendo", default='patients_profile/right_side_smiling/default_image.jpeg', upload_to='patients_profile/right_side_smiling')
    left_side = models.ImageField(
        verbose_name="lateral_izquierda", default='patients_profile/left_side/default_image.jpeg', upload_to='patients_profile/left_side')
    left_side_smiling = models.ImageField(
        verbose_name="lateral_izquierda_sonriendo", default='patients_profile/left_side_smiling/default_image.jpeg', upload_to='patients_profile/left_side_smiling')
    upper_oclusal = models.ImageField(
        verbose_name="oclusal_superior", default='patients_profile/upper_oclusal/default_image.jpeg', upload_to='patients_profile/upper_oclusal')
    lower_oclusal = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/lower_oclusal/default_image.jpeg', upload_to='patients_profile/lower_oclusal')
    front_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/front_intraoral/default_image.jpeg', upload_to='patients_profile/front_intraoral')
    right_side_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral')
    left_side_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral')
    panoramic_xray = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/panoramic_xray/default_image.jpeg', upload_to='patients_profile/panoramic_xray')
    lateral_xray = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/lateral_xray/default_image.jpeg', upload_to='patients_profile/lateral_xray')
    extra_photo1 = models.ImageField(verbose_name="imagen_extra1", default='patients_profile/extra_photo1/default_image.jpeg', upload_to='patients_profile/extra_photo1')
    extra_photo2 = models.ImageField(verbose_name="imagen_extra1", default='patients_profile/extra_photo2/default_image.jpeg', upload_to='patients_profile/extra_photo2')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PatientImage'
        verbose_name_plural = 'PatientImages'

    def __str__(self):
        return f'Set de fotografías {self.created}'
    
    # para guardar las imágenes
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
