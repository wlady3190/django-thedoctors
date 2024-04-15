from django.shortcuts import render

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# from doctors.forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name='appointment/dashboard.html'
    login_url=reverse_lazy('login')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')