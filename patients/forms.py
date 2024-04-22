from django import forms
from core import settings
from doctors.validators import letter_validator, numeric_validator
from patients.models import Patient, Medical_History



class DateInput(forms.DateInput):
    input_type = 'date'

class PatientProfileForm(forms.ModelForm):
    SEX_CHOICES = [
        ('MASCULINE', "masculino"),
        ('FEMENINE', "femenino")
    ]
    first_name = forms.CharField(max_length=150, validators=[letter_validator], widget=forms.TextInput(attrs={'placeholder': 'Juan Fernando', 'id': 'nombres'}))
    last_name = forms.CharField(max_length=150,  validators=[letter_validator], widget=forms.TextInput(attrs={'id':'apellidos'}))
    birthDate = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS)
    identification = forms.CharField(
        max_length=10)
    address = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, validators=[numeric_validator])
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Patient
        fields = ['first_name',
                  'last_name',
                  'birthDate',
                  'identification',
                  'address',
                  'email',
                  'phone',
                  'sex',]
        
class PatientClinicalHistoryForm(forms.ModelForm):
    
    allergy = forms.CharField(widget=forms.Textarea)
    diseases = forms.CharField(widget=forms.Textarea)
    medicines = forms.CharField(widget=forms.Textarea)
    additional_info = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Medical_History
        fields = ['allergy', 'diseases', 'medicines', 'additional_info',]