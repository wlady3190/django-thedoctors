from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from doctors.models import Doctor


#Formulario para creación de perfil de Doctor
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']



#Para actualizar el correo en caso de perdida        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

# Actualizar foto de perfil

class ProfileUpdateForm (forms.ModelForm):
   class Meta:
       model = Doctor
       fields = ['photo']