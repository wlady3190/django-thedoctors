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
    birthDate = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS, required=False)
    identification = forms.CharField(max_length=10, required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=15, validators=[numeric_validator], required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect(), required=False)

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
    
    allergy = forms.CharField(widget=forms.Textarea, required=False)
    diseases = forms.CharField(widget=forms.Textarea, required=False)
    medicines = forms.CharField(widget=forms.Textarea, required=False)
    additional_info = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Medical_History
        fields = ['allergy', 'diseases', 'medicines', 'additional_info',]