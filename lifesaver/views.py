from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Nurse, Patient
from django.http import HttpResponse

# Create your views here.
def index(request):
    patient = Patient.objects.all()
    nurse = Nurse.objects.all()
    doctor = Doctor.objects.all()

    total_patient = patient.count()
    sick = patient.filter(status='Sick').count()
    healing = patient.filter(status='Healing').count()
    cured = patient.filter(status='Cured').count()

    total_nurse = nurse.count()

    # if request.method == 'POST':
    #     form = 

    context = {
        'patient':patient, 'nurse':nurse,
        'doctor':doctor, 'total_patient':total_patient,
        'sick':sick, 'healing':healing, 'cured':cured,
        'total_nurse':total_nurse
    }

    return render(request, 'lifesaver/index.html', context)

def patient(request):
    patient = Patient.objects.all()

    total_patient = patient.count()

    context = {
        'patient':patient,
        'total_patient':total_patient
    }
    return render(request, 'lifesaver/patient.html', context)