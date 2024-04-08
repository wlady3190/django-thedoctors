from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import  UserRegisterForm





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



def login(request):
    pass
