from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import  ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created')
            return redirect('homepage')
    else:
        form  = UserRegisterForm()
    return render(request, 'doctors/register.html', {'form':form} )
#Para que se guarden adecuadamente el perfil y se cree, se genera una señal (signal)


@login_required
def profile(request):
    #update info y fotografia
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    # si no se quiere actualizar, solo se extraen los campos al form
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
    context = {
        'u_form':u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
