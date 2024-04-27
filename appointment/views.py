from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# from doctors.forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.views.generic import CreateView, ListView, View
from doctors.models import Doctor
from patients.models import Patient

from patients.models import Patient

from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from core.utils import test_func
# Create your views here.


def custom_404_error(request, exception):
    return render(request, 'error_pages/error_404.html', status = 404 )

   

class HomeView(View, LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request):
        user = request.user
        last_login = user.last_login
        doctor = Doctor.objects.filter(user = user)
        patients = Patient.objects.filter(user = user).order_by('-created')[:5]
        appointments = Appointment.objects.filter(user=user).order_by('-created')[:5]

        
        context = {
            'doctor': doctor,
            'patients': patients,
            'appointments': appointments,
            'last_login': last_login
        }
        return render(request, 'dashboard/dashboard.html', context)
    
    # def test_func(self):
    #     patient = Patient.objects.get(user = self.request.user)
    #     return patient == self.get_object()


    


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# class CreateAppointmentView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
#     template_name = 'appointment/medical_record.html'
#     context_object_name = 'objects'
#     model = Appointment
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user = self.request.user)


class CreateAppointmentView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'appointment/medical_record.html'
    form_class = AppointmentForm
    model = Appointment
    success_url = reverse_lazy('patient-read')

    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        form.instance.patient = patient
        messages.success(self.request, 'Cita médica generada con éxito')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    # def test_func(self):
    #     appointment = Appointment.objects.get(user= self.request.user) 
    #     return appointment == self.get_object()

class CreateAppointmentByPatientListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'appointment/appointment_list.html'
    model = Appointment
    context_object_name = 'appointments'

    
    
    def get_context_data(self, **kwargs):
        patient_id = self.kwargs['pk']        
        appointments = Appointment.objects.filter(patient_id = patient_id)
        context = {
            'appointments': appointments,
            'patient_id': patient_id
        }
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    

    def test_func(self):
        patient_id = self.kwargs.get('pk')
        patient = get_object_or_404(Patient, patient_id)
        return patient == self.request.user

      
