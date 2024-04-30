from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Schedule (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name='nombre_paciente', blank=True)
    appointment_date = models.DateField(default=date.today, blank=True, verbose_name='fecha_consulta')
    appointment_time = models.TimeField(default=None, blank=True, null=True, verbose_name='hora_consulta')
    
    def __str__(self):
        return f'cita {self.full_name}, fecha: {self.date_appointment}'
    
    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        ordering = ['-appointment_date']
    
    