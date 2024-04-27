from django import forms

from patients_images.models import Patientimage

class PatientImageForm(forms.ModelForm):
    
    #! extraorales Frontal
    front = forms.ImageField(required=False)
    front_smiling = forms.ImageField(required=False)
    #! extraorales lateral derecha
    right_side = forms.ImageField(required=False)
    right_side_smiling = forms.ImageField(required=False)
    
    #! extraorales lateral izquierda
    left_side = forms.ImageField(required=False)
    left_side_smiling = forms.ImageField(required=False )
    
    
    #! intraorales
    front_intraoral = forms.ImageField(required=False)
    right_side_intraoral = forms.ImageField(required=False)
    left_side_intraoral = forms.ImageField(required=False)
    upper_oclusal = forms.ImageField(required=False)
    lower_oclusal = forms.ImageField(required=False)
    
    
    #! radiografia
    panoramic_xray = forms.ImageField(required=False)
    lateral_xray = forms.ImageField(required=False)
    
    #! extras
    extra_photo1 = forms.ImageField(required=False)
    extra_photo2 = forms.ImageField(required=False)
    
    
    
    class Meta:
        model = Patientimage
        fields = ['front', 'front_smiling', 'right_side', 'right_side_smiling','left_side', 'left_side_smiling','front_intraoral', 'right_side_intraoral', 'left_side_intraoral','upper_oclusal', 'lower_oclusal', 'panoramic_xray', 'lateral_xray', 'extra_photo1', 'extra_photo2']