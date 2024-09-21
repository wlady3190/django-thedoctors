from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from core import settings
from doctors.models import Doctor
from .validators import letter_validator, numeric_validator


#Formulario para creación de perfil de Doctor
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Enter a valid email' ) 
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'


class UserAndProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, validators=[letter_validator], widget=forms.TextInput(attrs={'placeholder': 'Wladimir'}) )
    last_name = forms.CharField(max_length=50, validators=[letter_validator], widget=forms.TextInput(attrs={'placeholder': 'Tierra'}))
    # Campos del modelo de perfil (Profile)
    birthDate = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS, required=False)
    identification = forms.CharField(max_length=15, validators=[numeric_validator], required=False, widget=forms.TextInput(attrs={'placeholder': '1700000002'}))
    registryCode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': '1700000002'}))
    specialty = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Odontólogo'}))
    address = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Quito, Sector Tumbaco'}))
    phone = forms.CharField(max_length=15, validators=[numeric_validator], required=False, widget=forms.TextInput(attrs={'placeholder': '0990000001'}))
    photo = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        widgets = {'my_date_field': DateInput()}
        #! Este es el original model = User
        model = Doctor
        fields = ['first_name', 'last_name', 'birthDate', 'identification', 'registryCode','specialty', 'address', 'phone', 'photo']
