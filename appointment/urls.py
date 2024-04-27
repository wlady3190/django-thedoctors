from django.urls import path
# from .views import  profile
from doctors import views as doctors_views
from django.contrib.auth import views as auth_views
from appointment import views as appointment_views
from patients import views as patient_views
from patients_images import views as patient_images_views

# from doctors import views as views_doctor



urlpatterns = [
    # path('', appointment_views.DashboardView.as_view(), name='dashboard'),
    # path('', appointment_views.home_view, name='dashboard'),
    path('', appointment_views.HomeView.as_view(), name='dashboard'),
    
    
    #path('profile/', profile, name='profile' ),
    path('profile/', doctors_views.ProfileUpdateView.as_view(), name='profile' ),
    path('logout/', appointment_views.user_logout, name='logout'),
    # path('patient-options/', patient_views.ViewPatientsOptions.as_view(), name='patients_menu'),
    path('patient/new-patient/', patient_views.CreatePatientsView.as_view(), name='patient_new'),
    # path('patient-menu/', patient_views.ViewPatientsOptions.as_view(), name='patient-menu' ),
    path('patient/new/', patient_views.CreatePatientsView.as_view(), name='patient-create' ),
    #path('patient/<str:username>/', patient_views.ReadPatientsView.as_view(), name='patient-read'),
    path('patient/list/', patient_views.ReadPatientsView.as_view(), name='patient-read'),
    
    path('patient/<int:pk>/update/',patient_views.UpdatePatientsView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', patient_views.DeletePatientView.as_view(), name='patient-delete'),
    path('patient/<int:pk>/history/new/', patient_views.CreateMedicalHistoryView.as_view(), name='history-create'),
    path('patient/<int:pk>/history/detail/', patient_views.HistoryDetailView.as_view(), name='history-read'),
    path('patient/<int:pk>/history/update/', patient_views.UpdateMedicalHistoryView.as_view(), name='history-update'),
    path('patient/<int:pk>/appointment/create/', appointment_views.CreateAppointmentView.as_view(), name='appointment-create'),
    path('patient/<int:pk>/appointment/list/', appointment_views.CreateAppointmentByPatientListView.as_view(), name='appointment-read-list'),
    path('patient/<int:pk>/images-set/create/', patient_images_views.CreatePatientImageView.as_view(), name='images-repo-create'),
    path('patient/<int:pk>/images-set/read/', patient_images_views.CreatePatientImageListView.as_view(), name='images-repo-read'),
    path('patient/<int:pk>/images-set/<int:pk_image_set>/detail/', patient_images_views.CreatePatientImageView.as_view(), name='images-repo-detail'),
    path('patient/<int:pk>/images-set/<int:pk_image_set>/update/', patient_images_views.UpdatePatientImageView.as_view(), name='images-repo-update'),
    path('patient/<int:pk>/images-set/<int:pk_image_set>/delete/', patient_images_views.DeletePatientImageView.as_view(), name='images-repo-delete'),
    
    
    
    
        
    
]