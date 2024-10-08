"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

from django.conf.urls import handler404

from homepage import views as home_view
from doctors import views as doctors_views
from appointment.views import custom_404_error



handler404 = custom_404_error

urlpatterns = [
    path('admin-theokara-wlady3190-teeth-soft/', admin.site.urls),
    path('', home_view.home, name='homepage' ),
    path('register/', doctors_views.SignUpView.as_view(), name='register' ),
    path('login/', auth_views.LoginView.as_view(template_name = 'doctors/login.html'), name='login'),
    path('dashboard/', include('appointment.urls'), name='dashboard'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


