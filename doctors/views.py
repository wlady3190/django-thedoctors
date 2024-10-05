
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView, View

from doctors.models import Doctor
from .forms import   UserAndProfileUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from core.utils import test_func
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache




class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'doctors/register.html'




@method_decorator(never_cache, name='dispatch') 
class ProfileUpdateView (LoginRequiredMixin, UpdateView):
    template_name = 'appointment/profile.html'  
    model = Doctor
    form_class = UserAndProfileUpdateForm  


    def get_object(self, queryset=None):
        return self.request.user.doctor

    def get_success_url(self):
        return reverse('profile') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente')
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)
    
    def test_func(self):
        doctor = Doctor.objects.get(user = self.request.user) 
        return doctor == self.get_object()
    
    









