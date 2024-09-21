from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from datetime import time
from PIL import Image
from django.core.files.base import ContentFile
# Create your models here.


class Patientimage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    front = models.ImageField(
        verbose_name="foto_frontal", default='patients_profile/front/default_image.jpeg',
        upload_to='patients_profile/front', max_length=255)
    front_smiling = models.ImageField(
        verbose_name="frontal_sonriendo", default='patients_profile/front_smiling/default_image.jpeg', upload_to='patients_profile/front_smiling', max_length=255)
    right_side = models.ImageField(
        verbose_name="lateral_derecha", default='patients_profile/rigth_side/default_image.jpeg', upload_to='patients_profile/rigth_side', max_length=255)
    right_side_smiling = models.ImageField(
        verbose_name="lateral_derecha_sonriendo", default='patients_profile/right_side_smiling/default_image.jpeg', upload_to='patients_profile/right_side_smiling', max_length=255)
    left_side = models.ImageField(
        verbose_name="lateral_izquierda", default='patients_profile/left_side/default_image.jpeg', upload_to='patients_profile/left_side', max_length=255)
    left_side_smiling = models.ImageField(
        verbose_name="lateral_izquierda_sonriendo", default='patients_profile/left_side_smiling/default_image.jpeg', upload_to='patients_profile/left_side_smiling', max_length=255)
    upper_oclusal = models.ImageField(
        verbose_name="oclusal_superior", default='patients_profile/upper_oclusal/default_image.jpeg', upload_to='patients_profile/upper_oclusal', max_length=255)
    lower_oclusal = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/lower_oclusal/default_image.jpeg', upload_to='patients_profile/lower_oclusal', max_length=255)
    front_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/front_intraoral/default_image.jpeg', upload_to='patients_profile/front_intraoral', max_length=255)
    right_side_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral', max_length=255)
    left_side_intraoral = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral', max_length=255)
    panoramic_xray = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/panoramic_xray/default_image.jpeg', upload_to='patients_profile/panoramic_xray', max_length=255)
    lateral_xray = models.ImageField(
        verbose_name="oclusal_inferior", default='patients_profile/lateral_xray/default_image.jpeg', upload_to='patients_profile/lateral_xray', max_length=255)
    extra_photo1 = models.ImageField(verbose_name="imagen_extra1", default='patients_profile/extra_photo1/default_image.jpeg', upload_to='patients_profile/extra_photo1', max_length=255)
    extra_photo2 = models.ImageField(verbose_name="imagen_extra1", default='patients_profile/extra_photo2/default_image.jpeg', upload_to='patients_profile/extra_photo2', max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'PatientImage'
        verbose_name_plural = 'PatientImages'

    def __str__(self):
        return f'Set de fotografías {self.created}'
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Lista de campos de imagen a comprimir
        image_fields = [
            self.front,
            self.front_smiling,
            self.right_side,
            self.right_side_smiling,
            self.left_side,
            self.left_side_smiling,
            self.upper_oclusal,
            self.lower_oclusal,
            self.front_intraoral,
            self.right_side_intraoral,
            self.left_side_intraoral,
            self.panoramic_xray,
            self.lateral_xray,
            self.extra_photo1,
            self.extra_photo2,
        ]

        for image_field in image_fields:
            if image_field and hasattr(image_field, 'path'):
                img = Image.open(image_field.path)

                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                max_width, max_height = 1920, 1080
                img.thumbnail((max_width, max_height), Image.LANCZOS)

                # Comprimir la imagen
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=85)  
                
                image_field.save(image_field.name, ContentFile(buffer.getvalue()), save=False)
                buffer.close()

        super().save(*args, **kwargs)