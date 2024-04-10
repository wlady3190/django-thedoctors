from django.shortcuts import render

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# from doctors.forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.

# @login_required
# def dashboard(request):
#     return render(request, 'appointment/dashboard.html')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name='appointment/dashboard.html'
    login_url=reverse_lazy('login')
    


# @login_required
# def profile(request):

#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST,instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance= request.user.profile )
#         print('Post', request.POST)
#         print('Files:',request.FILES)
#         if u_form.is_valid() and p_form.is_valid():
#             print(u_form.is_valid())
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

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')