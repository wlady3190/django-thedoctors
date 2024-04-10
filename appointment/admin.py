from django.contrib import admin
from .models import Appointment, Diagnosis, Patient, Treatment, Vital_sign
# Register your models here.

admin.site.register([Appointment, Diagnosis,
                     Treatment, Vital_sign])
