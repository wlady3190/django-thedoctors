from django.db import models

# Create your models here.


class Images(models.Model):
    imagen1 = models.ImageField(default='imagen1', upload_to='/imagen1')
    imagen2 = models.ImageField(default='imagen2', upload_to='/imagen2')
    imagen3 = models.ImageField(default='imagen3', upload_to='/imagen3')
    imagen4 = models.ImageField(default='imagen4', upload_to='/imagen4')
    imagen5 = models.ImageField(default='imagen5', upload_to='/imagen5')
    imagen6 = models.ImageField(default='imagen6', upload_to='/imagen6')
    