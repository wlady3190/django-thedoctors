from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from appointment_schedule.forms import CreateScheduleForm
from appointment_schedule.models import Schedule
from django.contrib import messages


# Create your views here.


class CreateScheduleView(CreateView):
    template_name = 'appointment_schedule/schedule_create_form.html'
    model = Schedule
    form_class = CreateScheduleForm
    success_url = reverse_lazy('schedule-read')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Cita generada con éxito')       
        return super().form_valid(form)
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)

class ListScheduleView(ListView):
    template_name = 'appointment_schedule/schedule_list.html'
    model = Schedule
    context_object_name = 'schedule_list'


class DeleteScheduleView(DeleteView):
    model = Schedule
    template_name = 'appointment_schedule/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule-read')
    context_object_name = 'schedule'
    
    def delete(self, request,  *args, **kwargs):
        messages.success(self.request, 'Registro eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
