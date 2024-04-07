from django.shortcuts import render
from django.urls import path

from doctors.views import register

# Create your views here.

urlpatterns = [
    path('register', register, name = 'register_form' ),
    #path('login')
]