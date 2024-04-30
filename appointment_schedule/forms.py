from django import forms

from appointment_schedule.models import Schedule
from core import settings


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateScheduleForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=False)
    appointment_date = forms.DateField(widget=DateInput, input_formats=settings.DATE_INPUT_FORMATS, required=False)
    appointment_time = forms.TimeField(widget=TimeInput,required=False)
    
    
    class Meta:
        model = Schedule
        fields = ['full_name', 'appointment_date', 'appointment_time']