import re
from django.core.exceptions import ValidationError

def numeric_validator(value):
    pattern = r'^[0-9]*$'
    if not re.match(pattern, value):
        raise ValidationError('Ingrese solo números.')

def letter_validator(value):
    pattern = r'^[A-Za-z\s]*$'  # Permitir letras y espacios
    if not re.match(pattern, value):
        raise ValidationError('Ingrese solo letras.')