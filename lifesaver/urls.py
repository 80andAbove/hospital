from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('patient/', views.patient, name='patient'),
    path('patient/patient_add/', views.patient_add, name='patient_add'),
    path('patient/patient_update/<str:pk>', views.patient_update, name='patient_update'),
    path('department/', views.department, name='department'),
]