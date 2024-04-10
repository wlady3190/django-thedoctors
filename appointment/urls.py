from django.urls import path
# from .views import  profile

from doctors import views as doctors_views

from django.contrib.auth import views as auth_views
from appointment import views as appointment_views

# from doctors import views as views_doctor



urlpatterns = [
    path('', appointment_views.DashboardView.as_view(), name='dashboard'),
    #path('profile/', profile, name='profile' ),
    path('profile/', doctors_views.ProfileUpdateView.as_view(), name='profile' ),
    path('logout/', appointment_views.user_logout, name='logout'),

    
    
]