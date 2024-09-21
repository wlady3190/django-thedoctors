from django import forms

from appointment.models import Appointment
from core import settings

from doctors.validators import letter_validator, numeric_validator



class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    
    #!Signos vitales
    blood_pressure = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '120/80'}))
    heart_rate = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': '60'}))
    temperature = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'placeholder': '36.5'}))
    breathing_frequency = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': '60'}))
    oxygen_saturation = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': '99'}))
    # !Diagnóstico
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
    diagnosis_type = forms.ChoiceField(
        choices=DIAGNOSIS_TYPE,  widget=forms.RadioSelect,required=False)
    cie10_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Z012'}), required=False)
    diagnoses = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Examen odontológico'}), required=False)
    
    #!Complicaciones
    diagnoses_complications = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ingrese el diagnóstico y complicaciones detectados'}), required=False)
    procedures = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ingrese los procedimientos a ejecutarse'}), required=False)
    prescriptions = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ingrese los medicamentos prescritos'}), required=False)    
    appointment_date_generated = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS, required=False)
    
    
    class Meta:
        model = Appointment
        fields = ['blood_pressure', 'heart_rate', 'temperature',
                  'breathing_frequency', 'oxygen_saturation','diagnosis_type', 'cie10_code', 'diagnoses', 'diagnoses_complications', 'procedures', 'prescriptions','appointment_date_generated']
