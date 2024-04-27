# Generated by Django 5.0.3 on 2024-04-24 00:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0005_alter_patient_identification'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.ImageField(default='patients_profile/front/front.jpeg', upload_to='patients_profile/front', verbose_name='foto_frontal')),
                ('front_smiling', models.ImageField(default='patients_profile/front_smiling/front_smiling.jpeg', upload_to='patients_profile/front_smiling', verbose_name='frontal_sonriendo')),
                ('right_side', models.ImageField(default='patients_profile/rigth_side/right_side.jpeg', upload_to='patients_profile/rigth_side', verbose_name='lateral_derecha')),
                ('right_side_smiling', models.ImageField(default='patients_profile/right_side_smiling/right_side_smiling.jpeg', upload_to='patients_profile/right_side_smiling', verbose_name='lateral_derecha_sonriendo')),
                ('left_side', models.ImageField(default='patients_profile/left_side/left_side.jpeg', upload_to='patients_profile/left_side', verbose_name='lateral_izquierda')),
                ('left_side_smiling', models.ImageField(default='patients_profile/left_side_smiling/left_side_smiling.jpeg', upload_to='patients_profile/left_side_smiling', verbose_name='lateral_izquierda_sonriendo')),
                ('upper_oclusal', models.ImageField(default='patients_profile/upper_oclusal/upper_oclusal.png', upload_to='patients_profile/upper_oclusal', verbose_name='oclusal_superior')),
                ('lower_oclusal', models.ImageField(default='patients_profile/lower_oclusal/lower_oclusal.png', upload_to='patients_profile/lower_oclusal', verbose_name='oclusal_inferior')),
                ('front_intraoral', models.ImageField(default='patients_profile/front_intraoral/default_image.jpe', upload_to='patients_profile/front_intraoral', verbose_name='oclusal_inferior')),
                ('right_side_intraoral', models.ImageField(default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral', verbose_name='oclusal_inferior')),
                ('left_side_intraoral', models.ImageField(default='patients_profile/right_side_intraoral/default_image.jpeg', upload_to='patients_profile/right_side_intraoral', verbose_name='oclusal_inferior')),
                ('panoramic_xray', models.ImageField(default='patients_profile/panoramic_xray/default_image.jpeg', upload_to='patients_profile/panoramic_xray', verbose_name='oclusal_inferior')),
                ('lateral_xray', models.ImageField(default='patients_profile/lateral_xray/default_image.jpeg', upload_to='patients_profile/lateral_xray', verbose_name='oclusal_inferior')),
                ('extra_photo1', models.ImageField(default='patients_profile/extra_photo1/default_image.jpeg', upload_to='patients_profile/extra_photo1', verbose_name='imagen_extra1')),
                ('extra_photo2', models.ImageField(default='patients_profile/extra_photo2/default_image.jpeg', upload_to='patients_profile/extra_photo2', verbose_name='imagen_extra1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Patient_Image',
                'verbose_name_plural': 'Patient_Images',
            },
        ),
    ]