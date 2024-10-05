
from django.conf import settings
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseForbidden

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# from doctors.forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.views.generic import CreateView, ListView, View, DetailView

from doctors.models import Doctor
from patients.models import Patient, Medical_History
from appointment_schedule.models import Schedule

from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from core.utils import test_func
from datetime import date

#! crear pdf
from django.template.loader import render_to_string
#! OJO QUE ESTA DEPENDENCIA NO ESTÁ RECONOCIDA PERO FUNCIONA
from weasyprint import HTML # type: ignore
import tempfile
from datetime import date, datetime
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# Create your views here.

def custom_404_error(request, exception):
    return render(request, 'error_pages/error_404.html', status = 404 )

   
@method_decorator(never_cache, name='dispatch') 
class HomeView(View, LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request):
        user = request.user
        last_login = user.last_login
        doctor = Doctor.objects.filter(user = user)
        patients = Patient.objects.filter(user = user).order_by('-created')[:5]
        appointments = Appointment.objects.filter(user=user).order_by('-created')[:5]
        schedules = Schedule.objects.filter(user = user).order_by('appointment_date')[:5]

        
        context = {
            'doctor': doctor,
            'patients': patients,
            'appointments': appointments,
            'last_login': last_login,
            'schedules': schedules
        }
        return render(request, 'dashboard/dashboard.html', context)
    
    # def test_func(self):
    #     return self.request.user.is_authenticated

    # def handle_no_permission(self):
    #     if self.request.user.is_authenticated:
    #         return HttpResponseForbidden("You do not have permission to view this page.")
    #     else:
    #         return redirect('login')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@method_decorator(never_cache, name='dispatch') 
class CreateAppointmentView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'appointment/medical_record.html'
    form_class = AppointmentForm
    model = Appointment
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        form.instance.patient = patient
        messages.success(self.request, 'Sesión médica generada con éxito')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, pk = patient_id)
        try:
            medical_history = Medical_History.objects.get(patient = patient)
        except Medical_History.DoesNotExist:    
            medical_history = None
            messages.error(self.request, 'Debe generar antecedentes médicos. Acciones > Crear antecedentes')
        context['patient'] = patient
        context['medical_history'] = medical_history
        
        return context
    
    def get_success_url(self):
        patient_id = self.kwargs['pk']
        return reverse_lazy('appointment-read-list', kwargs={'pk': patient_id})
        
@method_decorator(never_cache, name='dispatch') 
class CreateAppointmentByPatientListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'appointment/appointment_list.html'
    model = Appointment
    context_object_name = 'appointments'

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']        
        appointments = Appointment.objects.filter(patient_id = patient_id)
        patient = get_object_or_404(Patient, pk=patient_id)
        context = {
            'patient_id': patient_id,
            'appointments': appointments,
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
    
# ! Generación de pdf

@method_decorator(never_cache, name='dispatch') 
class ExportPDFView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Appointment
    
    def get_object(self):
        patient_id = self.kwargs['pk']
        pk_appointment = self.kwargs['pk_appointment']
        return get_object_or_404(Appointment, patient_id=patient_id, id = pk_appointment)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        doctor = Doctor.objects.filter(user = user)
        appointment = self.get_object()
        patient = appointment.patient
                
        context = {
            'appointment': appointment,
            'patient': patient,
            'doctor': doctor,
            'user': user, 
        }
        
        response = HttpResponse(content_type="application/pdf")
        today_date = date.today().strftime("%Y-%m-%d")
        response["Content-Disposition"] = f"attachment; filename=certificado_{today_date}-{patient.identification}.pdf"
        response['Content-Transfer_Encoding'] = 'binary'
        
       
        html_string = render_to_string('appointment/certificate.html', context=context, request=request)
        html = HTML(string=html_string)
        result = html.write_pdf()
        
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())
        return response