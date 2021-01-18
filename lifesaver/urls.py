from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('patient/', views.patient, name='patient'),
    path('patient/add/', views.patient_add, name='patient_add'),
    path('patient/patient_update/<str:pk>', views.patient_update, name='patient_update'),
    
    path('nurse/', views.nurse, name='nurse'),
    path('nurse/add', views.nurse_add, name='nurse_add'),

    path('department/', views.department, name='department'),
]