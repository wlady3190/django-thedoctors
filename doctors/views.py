from django.shortcuts import redirect, render
from .forms import UserCreationForm


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request, 'doctors/register.html', {'form':form} )