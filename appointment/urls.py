from django.urls import path
# from .views import  profile
from doctors import views as doctors_views
from django.contrib.auth import views as auth_views
from appointment import views as appointment_views
from patients import views as patient_views

# from doctors import views as views_doctor



urlpatterns = [
    path('', appointment_views.DashboardView.as_view(), name='dashboard'),
    #path('profile/', profile, name='profile' ),
    path('profile/', doctors_views.ProfileUpdateView.as_view(), name='profile' ),
    path('logout/', appointment_views.user_logout, name='logout'),
    # path('patient-options/', patient_views.ViewPatientsOptions.as_view(), name='patients_menu'),
    path('patient/new-patient/', patient_views.CreatePatientsView.as_view(), name='patient_new'),
    path('patient-menu/', patient_views.ViewPatientsOptions.as_view(), name='patient-menu' ),
    path('patient/new/', patient_views.CreatePatientsView.as_view(), name='patient-create' ),
    #path('patient/<str:username>/', patient_views.ReadPatientsView.as_view(), name='patient-read'),
    path('patient/list/', patient_views.ReadPatientsView.as_view(), name='patient-read'),
    
    path('patient/<int:pk>/update/',patient_views.UpdatePatientsView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', patient_views.DeletePatientView.as_view(), name='patient-delete'),
    path('patient/<int:pk>/history/new/', patient_views.CreateMedicalHistoryView.as_view(), name='history-create'),
    path('patient/<int:pk>/history/<int:history_pk>/', patient_views.HistoryDetailView.as_view(), name='history-read'),
    path('patient/<int:pk>/history/<int:history_pk>/update/', patient_views.UpdateMedicalHistoryView.as_view(), name='history-update'),
    path('patient/<int:pk>/history/<int:history_pk>/delete/', patient_views.HistoryDeleteView.as_view(), name='history-delete'),
    
    
    

    
    
]