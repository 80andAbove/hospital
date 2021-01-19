from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Nurse, Patient, Department, WorkShift
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

#All Patient Related

def patient(request):
    patient = Patient.objects.all()

    context = {'patient':patient}
    return render(request, 'lifesaver/patient.html', context)

def patient_add(request):

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
        return redirect('patient')

    context = {'form':form,}
    return render(request, 'lifesaver/patient_add.html', context)

def patient_update(request, pk):

    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            print('Update completed')
            form.save()
            return redirect('patient')
        else:
            print('Update not completed')
            print(form.errors)
            
    context = {'form':form}

    return render(request, 'lifesaver/patient_update.html', context)

# Nurse Related

def nurse(request):
    nurse = Nurse.objects.all()
    workshift = WorkShift.objects.all()
    department = Department.objects.all()

    context = {'nurse':nurse, 'workshift':workshift, 'department':department}
    return render(request, 'lifesaver/nurse.html', context)
    

def nurse_add(request):
    nurse = Nurse.objects.all()
    form = NurseForm()

    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            print("Nurse Form is Valid")
            form.save()
        else:
            print("Nurse Form is Invalid")
            print(form.errors)
        return redirect('nurse')

    context = {'form':form,}
    return render(request, 'lifesaver/nurse_add.html', context)

#Work Related

def department(request):
    department = Department.objects.all()

    context = {'department':department}
    return render(request, 'lifesaver/department.html', context)