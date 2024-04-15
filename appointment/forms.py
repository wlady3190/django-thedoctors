from django import forms

from appointment.models import Diagnosis, Treatment, Vital_Signs


class VitalSignForm (forms.ModelForm):
    blood_pressure = forms.CharField(
        max_length=7, default=0, blank=True)
    heart_rate = forms.PositiveSmallIntegerField(
        default=0, blank=True)
    temperature = forms.PositiveDecimalField(
        default=0.0, decimal_places=1, max_digits=3, blank=True)
    breathing_frequency = forms.PositiveSmallIntegerField(
        default=0, blank=True)
    oxygen_saturation = forms.PositiveSmallIntegerField(
        default=0,  blank=True)

    class Meta:
        model = Vital_Signs
        fields = ['blood_pressure', 'heart_rate', 'temperature',
                  'breathing_frequency', 'oxygen_saturation']


class DiagnosisForm(forms.ModelForm):
    DIAGNOSIS_TYPE = [
        ('PRE', 'presuntivo'),
        ('DEF', 'definitivo')]
    diagnosis_type = forms.ChoiceField(
        choices=DIAGNOSIS_TYPE, max_length=25, widget=forms.RadioSelect)
    cie10_code = forms.CharField(
        max_length=6, blank=True)
    description = forms.TextField()
    
    class Meta:
        model= Diagnosis
        fields = ['diagnosis_type', 'cie10_code', 'description']


class TreatmentForm(forms.ModelForm):
    diagnoses = forms.TextField()
    complications = forms.TextField()
    procedures = forms.TextField()
    prescriptions = forms.TextField()
    
    class Meta:
        model = Treatment
        fields = ['diagnoses', 'complications', 'procedures', 'prescriptions']
    
    