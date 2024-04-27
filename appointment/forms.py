from django import forms

from appointment.models import Appointment
from core import settings

from doctors.validators import letter_validator, numeric_validator



class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    
    #!Signos vitales
    blood_pressure = forms.CharField(required=False)
    heart_rate = forms.IntegerField(required=False)
    temperature = forms.IntegerField(required=False)
    breathing_frequency = forms.IntegerField(required=False)
    oxygen_saturation = forms.IntegerField(required=False)
    # !Diagnóstico
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
    diagnosis_type = forms.ChoiceField(
        choices=DIAGNOSIS_TYPE,  widget=forms.RadioSelect,required=False)
    cie10_code = forms.CharField()
    diagnoses = forms.CharField(widget=forms.Textarea, required=False)
    
    #!Complicaciones
    diagnoses_complications = forms.CharField(widget=forms.Textarea, required=False)
    procedures = forms.CharField(widget=forms.Textarea, required=False)
    prescriptions = forms.CharField(widget=forms.Textarea, required=False)    
    appointment_date_generated = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS, required=False)
    
    
    class Meta:
        model = Appointment
        fields = ['blood_pressure', 'heart_rate', 'temperature',
                  'breathing_frequency', 'oxygen_saturation','diagnosis_type', 'cie10_code', 'diagnoses', 'diagnoses_complications', 'procedures', 'prescriptions','appointment_date_generated']
