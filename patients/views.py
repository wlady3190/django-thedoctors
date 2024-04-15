from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from patients.forms import PatientProfileForm,  PatientClinicalHistoryForm

from patients.models import Medical_History, Patient
# Create your views here.


# * MOSTRAR MENU DE PACIENTES
class ViewPatientsOptions(TemplateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients/patients_menu.html'

# * CRUD PACIENTES
# * CREAR PACIENTES

class CreatePatientsView(CreateView, LoginRequiredMixin, UserPassesTestMixin ):
    template_name = 'patients/patients_form.html'
    model = Patient
    success_url = reverse_lazy('patient-read')
    form_class = PatientProfileForm
    
    
    def form_valid(self, form):
        #para que el usuario sea el doctor logueado
        form.instance.doctor = self.request.user
        messages.success(self.request, 'Paciente añadido con éxito')
        return super().form_valid(form)

# * ACTUALIZAR PACIENTES

class UpdatePatientsView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients/patients_update_form.html'
    model = Patient
    success_url = 'patients/patients_form.html'
    form_class = PatientProfileForm
    
    def form_valid(self, form) :
        form.instance.doctor  = self.request.user
        return super().form_valid(form)
    
    #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False

# * LISTAR TODOS LOS PACIENTES 

class ReadPatientsView(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = Patient
    template_name = 'patients/patients_list.html'
    context_object_name = 'patients'
    # ordering = ['last_name']
    # paginate_by = 5
    
# * BORRAR PACIENTE
class DeletePatientView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Patient
    success_url = 'patients/patients_list.html'
    
        #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
# ** HISTORIAL MEDICO **
# * CREAR HISTORIAL

class CreateMedicalHistoryView(CreateView, LoginRequiredMixin, UserPassesTestMixin ):
    template_name = 'patients/historial_form.html'
    model = Medical_History
    success_url = 'patients/historial_form.html'
    form_class = PatientProfileForm
    
    
    def form_valid(self, form):
        #para que el usuario sea el doctor logueado
        form.instance.doctor = self.request.user
        messages.success(self.request, 'Paciente añadido con éxito')
        return super().form_valid(form)


# * ACTUALIZAR HISTORIA MEDICA


class UpdateMedicalHistoryView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients/historial_update_form.html'
    model = Medical_History
    success_url = 'patients/historial_form.html'
    form_class = PatientClinicalHistoryForm
        
    #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False

# * LISTAR HISTORIAL

class HistoryDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Medical_History
    template_name = 'patients/historial_detail.html'


# * ELIMINAR HISTORIAL 

class HistoryDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Medical_History
    success_url = 'patients/patients_list.html'
    
        #Evitar que doctores ajenos accedan a pacientes
    def test_func(self):
        patient  = self.get_object()
        if self.request.user == patient.doctor:
            return True
        return False
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado con éxito')
        return super().delete(request, *args, **kwargs)

    
    

