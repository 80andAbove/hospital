from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Doctor, Nurse, Patient, Department, WorkShift
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import DoctorForm, NurseForm, PatientForm, CreateUserForm

#Welcome page
def welcome(request):
    context = {}
    return render(request, 'lifesaver/welcome.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Registeration success")
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
        else:
            print("Registeration failed")
            print(form.errors)
            messages.info(request, "Could not register")
            return redirect('register')
        return redirect('login')

    context = {'form':form}
    return render(request, 'lifesaver/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
        print("Success")
    else:
        print("Failed")
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            print("Failed 1")

            if user is not None:
                login(request, user)
                return redirect('index')
                print("Failed 2")
            
            else:
                messages.info(request, 'Username or Password is Incorrect')
                print("Failed 3")

    context = {}
    return render(request, 'lifesaver/login.html', context)

def forgot_pw(request):
    
    context = {}
    return render(request, 'lifesaver/forgot_pw.html', context)

def logout(request):
    context = {}
    return render(request, 'lifesaver/logout.html', context)

# Create your views here.
def index(request):
    patients = Patient.objects.all()
    nurses = Nurse.objects.all()
    doctors = Doctor.objects.all()
    department = Department.objects.all()

    total_patient = patients.count()
    sick = patients.filter(status='Sick').count()
    healing = patients.filter(status='Healing').count()
    cured = patients.filter(status='Cured').count()

    total_nurse = nurses.count()

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

#All Doctor Related

def doctor(request):

    doctors = Doctor.objects.all()

    context = {'doctors':doctors}
    return render(request, 'lifesaver/doctor.html', context)

def doctor_add(request):
    
    doctors = Doctor.objects.all()
    form = DoctorForm()

    context = {'doctors':doctors, 'form':form}

    return render(request, 'lifesaver/doctor_add.html', context)

def doctor_update(request):

    doctors = Doctor.objects.all(id=pk)
    form = DoctorForm(instance=doctors)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctors)
        if form.is_valid():
            print('Update completed')
            form.save()
            return redirect('doctor')
        else:
            print('Update not completed')
            print(form.errors)

    context = {'doctors':doctors, 'form':form}

    return render(request, 'lifesaver/doctor_update.html', context)

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
    nurses = Nurse.objects.all(id=pk)
    form = NurseForm(instance=nurses)

    if request.method == 'POST':
        form = NuseForm(request.POST, instance=nurses)
        if form.is_valid():
            print('Update completed')
            form.save()
            return redirect('nurse')
        else:
            print('Update not completed')
            print(form.errors)

    context = {'form':form}
    return render(request, 'lifesaver/nurse_update.html', context)

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

    context = {'form':form}
    return render(request, 'lifesaver/patient_add.html', context)

def patient_update(request, pk):

    patients = Patient.objects.get(id=pk)
    form = PatientForm(instance=patients)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patients)
        if form.is_valid():
            print('Update completed')
            form.save()
            return redirect('patient')
        else:
            print('Update not completed')
            print(form.errors)
            
    context = {'form':form}

    return render(request, 'lifesaver/patient_update.html', context)

#Work Related

def department(request):
    departments = Department.objects.all()

    context = {'departments':department}
    return render(request, 'lifesaver/department.html', context)