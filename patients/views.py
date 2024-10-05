from datetime import  datetime
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from patients.forms import PatientProfileForm,  PatientClinicalHistoryForm

from patients.models import Medical_History, Patient
from core.utils import test_func
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# * CRUD PACIENTES
# * CREAR PACIENTES
@method_decorator(never_cache, name='dispatch') 
class CreatePatientsView(CreateView, LoginRequiredMixin, UserPassesTestMixin ):
    template_name = 'patients/patients_form.html'
    model = Patient
    success_url = reverse_lazy('patient-read')
    form_class = PatientProfileForm
    
    
    
    def form_valid(self, form):
        #para que el usuario sea el doctor logueado
        form.instance.user = self.request.user
        if Patient.objects.filter(user = self.request.user, identification = form.cleaned_data['identification']).exists():
            messages.error(self.request, 'Ya existe un usuario con esa cedula')
            return self.form_invalid(form)
        messages.success(self.request, 'Paciente añadido con éxito')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def test_func(self):
        patient = Patient.objects.get(user = self.request.user)
        return patient == self.get_object()

# * ACTUALIZAR PACIENTES
@method_decorator(never_cache, name='dispatch') 
class UpdatePatientsView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients/patients_form.html'
    model = Patient
    success_url = reverse_lazy('patient-read')
    form_class = PatientProfileForm

    
    
    def form_valid(self, form) :
        form.instance.user  = self.request.user
        messages.success(self.request, 'Paciente actualizado con éxito')
        return super().form_valid(form)
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    #evitar que usuarios ajenos vean la info
    def test_func(self):
        patient = Patient.objects.get(user = self.request.user)
        return patient == self.get_object()
    

# * LISTAR TODOS LOS PACIENTES 
@method_decorator(never_cache, name='dispatch') 
class ReadPatientsView(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = Patient
    template_name = 'patients/patients_list.html'
    context_object_name = 'patients'
    
    

    def get_age(self, birthdate):
        today = datetime.now()
        age = today.year - birthdate.year -((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for patient in context['patients']:
            patient.age = self.get_age(patient.birthDate)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    # def test_func(self):
    #     patient = Patient.objects.get(user = self.request.user)
    #     return patient == self.get_object()
        
    
    
        
    
@method_decorator(never_cache, name='dispatch') 
class DeletePatientView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Patient
    template_name = 'patients/patients_confirm_delete.html'
    success_url =  reverse_lazy('patient-read')
  
        #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def test_func(self):
        patient = Patient.objects.get(user = self.request.user)
        return patient == self.get_object()
        
    
    
# ! HISTORIAL MEDICO **
# * CREAR HISTORIAL
@method_decorator(never_cache, name='dispatch') 
class CreateMedicalHistoryView(CreateView, LoginRequiredMixin, UserPassesTestMixin ):
    template_name = 'patients/history_form.html'
    model = Medical_History
    #fields = ['allergy', 'diseases', 'medicines', 'additional_info']
    form_class = PatientClinicalHistoryForm
    success_url = reverse_lazy('patient-read')

    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk=patient_id)
        form.instance.patient = patient
        form.save()
        messages.success(self.request, 'Historia creada con éxito')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def test_func(self):
        medical_history = Medical_History.objects.get(user = self.request.user)
        return medical_history == self.get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        context['patient'] = patient
        return context
        
        
    

# * ACTUALIZAR HISTORIA MEDICA

@method_decorator(never_cache, name='dispatch') 
class UpdateMedicalHistoryView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients/history_form.html'
    model = Medical_History
    success_url = reverse_lazy('patient-read')
    form_class = PatientClinicalHistoryForm

    
    
    
    def get_object(self, queryset= None):
        history_id = self.kwargs['pk']
        history = get_object_or_404(Medical_History, pk = history_id)
        return history
        
    def form_valid(self, form):
        messages.success(self.request, 'Historia actualizada con éxito')
        return super().form_valid(form)
        
    #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    # def test_func(self):
    #     medical_history = Medical_History.objects.get(user = self.request.user)
    #     return medical_history == self.get_object()
    
# #  LISTAR HISTORIAL
@method_decorator(never_cache, name='dispatch') 
class HistoryDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Medical_History
    template_name = 'patients/history_detail.html'
    context_object_name = 'patients'

    
     
    def get_object(self, queryset= None):
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        history = get_object_or_404(Medical_History, patient=patient)
        return history

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def test_func(self):
        medical_history = Medical_History.objects.get(user = self.request.user)
        return medical_history == self.get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        context['patient'] = patient
        return context
        


