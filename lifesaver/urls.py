from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='user_login'),
    path('forgot_pw/', views.forgot_pw, name='forgot_pw'),
    path('logout/', views.logout, name='logout'),
    
    #Homepage
    path('index/', views.index, name='index'),

    #Doctor Related
    path('doctor/', views.doctor, name='doctor'),
    path('doctor/add', views.doctor_add, name='doctor_add'),
    path('doctor/update/<str:pk>', views.doctor_update, name='doctor_update'),

    #Nurse Related
    path('nurse/', views.nurse, name='nurse'),
    path('nurse/add', views.nurse_add, name='nurse_add'),
    path('nurse/update/<str:pk>', views.nurse_update, name='nurse_update'),

    #Patient Related
    path('patient/', views.patient, name='patient'),
    path('patient/add/', views.patient_add, name='patient_add'),
    path('patient/patient_update/<str:pk>', views.patient_update, name='patient_update'),

    #Department Related
    path('department/', views.department, name='department'),
    path('department_new/', views.department_new, name='department_new'),
]