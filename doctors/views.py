
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView, View

from doctors.models import Profile
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
    model = Profile
    form_class = UserAndProfileUpdateForm  # Reemplaza 'ProfileUpdateForm' con el nombre de tu formulario de actualización

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('profile') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente')
        return super().form_valid(form)
    
    # template_name = 'appointment/profile.html'
    # context_object_name = 'user'
    # queryset = Profile.objects.all()
    # form_class = UserAndProfileUpdateForm

    
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileUpdateView, self).get_context_data(**kwargs)
    #     user = self.request.user
    #     context['p_form'] = UserAndProfileUpdateForm(instance=self.request.user.profile, initial={'first_name': user.first_name, 'last_name': user.last_name})
    #     return context
    
    # def form_valid(self, form):
    #     profile = form.save(commit=False)
    #     user = profile.user
    #     user.last_name = form.cleaned_data['last_name']
    #     user.first_name = form.cleaned_data['first_name']
    #     user.save()
    #     profile.save()
    
    #     return HttpResponseRedirect(reverse('dashboard', kwargs={'pk':self.get_object().id}))
    
    
    
    # template_name = 'appointment/profile.html'
    # context_object_name = 'user'
    # model = Profile
    # form_class = ProfileUpdateForm
    
    # def get_success_url(self):
    #     return reverse('dashboard', kwargs={'pk': self.get_object().id})
    
    
    # def get_context_data(self, **kwargs):
    #     context = super(ProfileUpdateView, self).get_context_data(**kwargs)
    #     context['user_form'] = UserUpdateForm(instance=self.request.user)
    #     return context
    
    
    # u_form  = UserUpdateForm
    # p_form = ProfileUpdateForm
    # template_name = 'appointment/profile.html'
    # def post(self, request, *args, **kwargs):
    #     post_data = request.POST or None
    #     file_data = request.FILES or None
    #     u_form  = UserUpdateForm(post_data, instance=request.user)
    #     p_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, 'Profile updated')
    #         return HttpResponseRedirect(reverse_lazy('dashboard'))
    #     context = self.get_context_data(
    #         u_form = u_form,
    #         p_form = p_form
    #     )
    #     return self.render_to_response(context)
    
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)



#from django.core.files.base import ContentFile


# class UserProfile(View):
#     template_name = 'profile.html'

#     def post(self, request):
#         try:
#             user_profile = Profile.objects.get(user=request.user)
#         except Profile.DoesNotExist:
#             user_profile = None
#         uploaded_image = request.FILES.get('photo', None)
#         if uploaded_image:
#             user_profile.profile_image.save(uploaded_image.name, ContentFile(uploaded_image.read()))
#         full_name = request.POST.get('name')
#         email = request.POST.get('email') 
#         designation = request.POST.get('designation')
#         mobile_number = request.POST.get('mobile_no')
#         profile_summary = request.POST.get('profile_summary')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         country = request.POST.get('country')

#         if user_profile:
#             user_profile.full_name = full_name
#             user_profile.designation = designation
#             user_profile.mobile_number = mobile_number
#             user_profile.profile_summary = profile_summary
#             user_profile.city = city
#             user_profile.state = state
#             user_profile.country = country
#             user_profile.save()

       
#             user_profile.user.email = email
#             user_profile.user.save()

#         return redirect('user-profile') 






    # def get(self, request):
    #     try:
    #         user_profile = Profile.objects.get(user=request.user)
    #     except Profile.DoesNotExist:
    #         user_profile = None
    #     form_data = {
    #         'name': user_profile.full_name if user_profile else '',
    #         'email': request.user.email if user_profile else '', 
    #         'designation': user_profile.designation if user_profile else '',
    #         'mobile_no': user_profile.mobile_number if user_profile else '',
    #         'profile_image': user_profile.profile_image if user_profile else '',
    #         'profile_summary': user_profile.profile_summary if user_profile else '',
    #         'city': user_profile.city if user_profile else '',
    #         'state': user_profile.state if user_profile else '',
    #         'country': user_profile.country if user_profile else '',
    #     }
    #     context = {
    #     'profile': user_profile,
    #     'form_data': form_data
    #     }
    #     return render(request, self.template_name, context)












