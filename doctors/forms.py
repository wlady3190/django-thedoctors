from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor



#Formulario para creación de perfil de Doctor
class UserCreationForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model = Doctor
        fields = [ 'email', 'password1', 'password2']

#Para actualizar el correo en caso de perdida        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = Doctor
        fields = ['email']

# Actualizar foto de perfil


class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['photo']