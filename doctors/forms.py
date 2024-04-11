from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from core import settings
from doctors.models import Profile


#Formulario para creación de perfil de Doctor
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Enter a valid email' ) 
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

# #Para actualizar el correo en caso de perdida        
# class UserUpdateForm(forms.ModelForm):  
#     class Meta:
#         model = User
#         fields = ['username','email']

# # Actualizar foto de perfil

# class ProfileUpdateForm (forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ['birthDate','identification','registryCode','address','phone','photo']
       

# class UserAndProfileUpdateForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField(max_length=200, help_text='Enter a valid email')
    
#     class Meta:
#         model = Profile
#         fields = ['birthDate','identification','registryCode','address','phone','photo']


class DateInput(forms.DateInput):
    input_type = 'date'


class UserAndProfileUpdateForm(forms.ModelForm):
    # Campos del modelo de usuario (User)
    
    numeric_validator = RegexValidator(r'^[0-9]*$', 'Identificación / teléfono: Ingresar solo números')
    letter_validator = RegexValidator(r'^[A-Za-z]*$', 'Nombre / Apellido: Ingresar solo letras')

    first_name = forms.CharField(max_length=50, validators=[letter_validator])
    last_name = forms.CharField(max_length=50, validators=[letter_validator])
    # Campos del modelo de perfil (Profile)
    birthDate = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS)
    identification = forms.CharField(max_length=15, validators=[numeric_validator])
    registryCode = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=15, validators=[numeric_validator])
    photo = forms.ImageField(widget=forms.FileInput)

    class Meta:
        widgets = {'my_date_field': DateInput()}
        model = User
        fields = ['first_name', 'last_name', 'birthDate', 'identification', 'registryCode', 'address', 'phone', 'photo']
