from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PatientImageForm
from.models import Patientimage
from patients.models import Patient
from django.contrib import messages
import logging

# Create your views here.


# ! Crear set de imagenes por paciente
class CreatePatientImageView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients_images/patients_images_form.html'
    form_class = PatientImageForm
    model = Patientimage
    success_url = reverse_lazy('patient-read')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        form.instance.patient = patient
        messages.success(self.request, 'Imágenes agregadas con éxito')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    # def test_func(self):
    #     appointment = Appointment.objects.get(user= self.request.user) 
    #     return appointment == self.get_object()

# ! Ver listado de imagenes por paciente
class CreatePatientImageListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'patients_images/patient_images_list.html'
    model = Patientimage
    context_object_name = 'patients_images'

    
    
    def get_context_data(self, **kwargs):
        patient_id = self.kwargs['pk']        
        patients_images = Patientimage.objects.filter(patient_id = patient_id)
        patient = get_object_or_404(Patient, pk = patient_id)
        context = {
            'patients_images': patients_images,
            'patient_id': patient_id,
            'patient': patient
        }
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    

    def test_func(self):
        patient_id = self.kwargs.get('pk')
        patient = get_object_or_404(Patient, patient_id)
        return patient == self.request.user


#! Ver y actualizar set de imagenes por ID

class UpdatePatientImageView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Patientimage
    form_class = PatientImageForm
    template_name = 'patients_images/patients_images_form.html'

    
    # def test_func(self):
        
    #     patient_image = self.get_object()
    #     return self.request.user == patient_image.user

    def get_object(self, queryset=None):
        # user = self.request.user
        patient_id = self.kwargs['pk']
        pk_image_set = self.kwargs['pk_image_set'] 
        print(pk_image_set)
        return get_object_or_404(Patientimage, patient_id=patient_id, id=pk_image_set) 


    def form_valid(self, form):
        messages.success(self.request, 'Set actualizado con éxito')
        return super().form_valid(form)
    
    def get_success_url(self):
        patient_id = self.kwargs['pk']
        return reverse_lazy('images-repo-read', kwargs={'pk': patient_id})
 
 
# todo Implementar Mixin    
    # def test_func(self):
    #     medical_history = Medical_History.objects.get(user = self.request.user)
    #     return medical_history == self.get_object()
    

class DeletePatientImageView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Patientimage
    template_name = 'patients_images/patient_images_confirm_delete.html'

    def get_object(self, queryset=None):
        # user = self.request.user
        patient_id = self.kwargs['pk']
        pk_image_set = self.kwargs['pk_image_set'] 
        return get_object_or_404(Patientimage, patient_id=patient_id, id=pk_image_set) 
    
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Registro eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
    def get_success_url(self):
        patient_id = self.kwargs['pk']
        return reverse_lazy('images-repo-read', kwargs={'pk': patient_id})
    
    
    
    
        #Evitar que doctores ajenos accedan a pacientes
    # def test_func(self):
    #     patient  = self.get_object()
    #     if self.request.user == patient.doctor:
    #         return True
    #     return False
    