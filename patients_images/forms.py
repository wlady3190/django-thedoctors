from django import forms

from patients_images.models import Patientimage

class PatientImageForm(forms.ModelForm):
    
    #! extraorales Frontal
    front = forms.ImageField(required=False, label='Frontal',widget=forms.FileInput)
    front_smiling = forms.ImageField(required=False, label='Front. sonriendo',widget=forms.FileInput,)
    #! extraorales lateral derecha
    right_side = forms.ImageField(required=False, label='Derecha',widget=forms.FileInput)
    right_side_smiling = forms.ImageField(required=False, label='Der. sonriendo', widget=forms.FileInput,)
    
    #! extraorales lateral izquierda
    left_side = forms.ImageField(required=False, label='Izquierda',widget=forms.FileInput,)
    left_side_smiling = forms.ImageField(required=False, label='Izq. sonriendo',widget=forms.FileInput, )
    
    
    #! intraorales
    front_intraoral = forms.ImageField(required=False, label='Int. Oral frontal',widget=forms.FileInput,)
    right_side_intraoral = forms.ImageField(required=False, label='Int. Oral Der.',widget=forms.FileInput,)
    left_side_intraoral = forms.ImageField(required=False, label='Int. Oral Izq.',widget=forms.FileInput,)
    upper_oclusal = forms.ImageField(required=False, label='Oclusal superior',widget=forms.FileInput,)
    lower_oclusal = forms.ImageField(required=False, label='Oclusal inferior',widget=forms.FileInput,)
    
    
    #! radiografia
    panoramic_xray = forms.ImageField(required=False, label='Panorámica',widget=forms.FileInput,)
    lateral_xray = forms.ImageField(required=False, label='Lateral',widget=forms.FileInput,)
    
    #! extras
    extra_photo1 = forms.ImageField(required=False, label='Extra 1',widget=forms.FileInput,)
    extra_photo2 = forms.ImageField(required=False, label='Extra 2',widget=forms.FileInput,)
    
    
    
    class Meta:
        model = Patientimage
        fields = ['front', 'front_smiling', 'right_side', 'right_side_smiling','left_side', 'left_side_smiling','front_intraoral', 'right_side_intraoral', 'left_side_intraoral','upper_oclusal', 'lower_oclusal', 'panoramic_xray', 'lateral_xray', 'extra_photo1', 'extra_photo2']