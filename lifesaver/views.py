from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Nurse, Patient, Department
from django.http import HttpResponse
from .forms import DoctorForm, NurseForm, PatientForm

# Create your views here.
def index(request):
    patient = Patient.objects.all()
    nurse = Nurse.objects.all()
    doctor = Doctor.objects.all()
    department = Department.objects.all()

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
        'total_nurse':total_nurse,
        'department':department
    }

    return render(request, 'lifesaver/index.html', context)

def patient(request):
    patient = Patient.objects.all()
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            print("Patient Form is Valid")
            form.save()
        else:
            print("Patient Form is Invalid")
            print(form.errors)
        return redirect('index')

    context = {
        'patient':patient,
        'form':form,
    }
    return render(request, 'lifesaver/patient.html', context)

def department(request):
    department = Department.objects.all()

    context = {'department':department}
    return render(request, 'lifesaver/department.html', context)