from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Nurse, Patient, Department, WorkShift
from django.http import HttpResponse
from .forms import DoctorForm, NurseForm, PatientForm

# Create your views here.
def index(request):
    patients = Patient.objects.all()
    nurses = Nurse.objects.all()
    doctors = Doctor.objects.all()
    department = Department.objects.all()

    total_patient = patient.count()
    sick = patient.filter(status='Sick').count()
    healing = patient.filter(status='Healing').count()
    cured = patient.filter(status='Cured').count()

    total_nurse = nurse.count()

    # if request.method == 'POST':
    #     form = 

    context = {
        'patients':patients, 'nurses':nurses,
        'doctors':doctors, 'total_patient ':total_patient,
        'sick':sick, 'healing':healing, 'cured':cured,
        'total_nurse':total_nurse,
        'department':department
    }

    return render(request, 'lifesaver/index.html', context)

#All Patient Related

def patient(request):
    patients = Patient.objects.all()

    context = {'patients':patients}
    return render(request, 'lifesaver/patient.html', context)

def patient_add(request):

    patients = Patient.objects.all()
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

    patients = Patient.objects.get(id=pk)
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

#All Doctor Related

def doctor(request):

    doctors = Doctor.object.all()

    context = {}
    return render(request, 'lifesaver/doctor.html', context)

def doctor_add(request):
    
    doctors = Doctor.object.all()
    form = DoctorForm()

    context = {'doctors':doctors, 'form':form}
    return render(request, 'lifesaver/doctor')

def doctor_update(request):

    doctors = Doctor.object.all()
    form = DoctorForm()

    context = {'doctors':doctors, 'form':form}

# Nurse Related

def nurse(request):
    nurses = Nurse.objects.all()
    workshift = WorkShift.objects.all()
    #department = Nurse.objects.get('sector')
    nurses_department = Nurse.objects.select_related('sector').all()

    context = {'nurses':nurses, 'workshift':workshift, 'nurses_department':nurses_department}
    return render(request, 'lifesaver/nurse.html', context)
    

def nurse_add(request):
    nurses = Nurse.objects.all()
    form = NurseForm()

    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            print("Nurse Form is Valid")
            form.save()
        else:
            print("Nurse Form is Invalid")
            print(form.errors)
        return redirect('nurses')

    context = {'form':form,}
    return render(request, 'lifesaver/nurse_add.html', context)

def nurse_update(request):
    nurses = Nurse.objects.all()
    form = NurseForm()

    context = {}
    return render(request, 'lifesaver/nurse_update.html', context)

#Work Related

def department(request):
    departments = Department.objects.all()

    context = {'departments':department}
    return render(request, 'lifesaver/department.html', context)