from django.contrib import admin
from .models import Patient, Medical_History
# Register your models here.
admin.site.register([Patient,  Medical_History])
