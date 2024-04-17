
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView, View

from doctors.models import Doctor
from .forms import   UserAndProfileUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView




# def register(request):
#     if request.method =='POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, 'Account created')
#             return redirect('homepage')
#     else:
#         form  = UserRegisterForm()
#     return render(request, 'doctors/register.html', {'form':form} )
# #Para que se guarden adecuadamente el perfil y se cree, se genera una señal (signal)

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'doctors/register.html'





# @login_required
# def profile(request):
#     #update info y fotografia
#     #doctor_profile, created = Doctor.objects.get_or_create(user = request.user)
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance= request.user.profile )
#         print(request.POST)
#         print(request.FILES)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('dashboard')
#     # si no se quiere actualizar, solo se extraen los campos al form
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance= request.user.profile)
#     context = {
#         'u_form':u_form,
#         'p_form': p_form
#     }
#     return render(request, 'appointment/profile.html', context)

class ProfileUpdateView (LoginRequiredMixin, UpdateView):
    template_name = 'appointment/profile.html'  # Reemplaza 'your_template.html' con el nombre de tu template
    model = Doctor
    form_class = UserAndProfileUpdateForm  # Reemplaza 'ProfileUpdateForm' con el nombre de tu formulario de actualización

    def get_object(self, queryset=None):
        return self.request.user.doctor

    def get_success_url(self):
        return reverse('profile') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente')
        return super().form_valid(form)
    
    
    









