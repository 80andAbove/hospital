from django import forms
from django.forms import ModelForm
from .models import Doctor, Nurse, Patient, Department, WorkShift
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Doctor',
            'class': 'form-control'
    }
    ))

#     department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs=
#     {
#             'class': 'selectpicker',
#             'placeholder': 'Department', 
#     }
#     )) 

    class Meta:
        model = Doctor
        fields = '__all__'

class NurseForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Nurse',
            'class': 'form-control'
    }
    ))

    class Meta:
        model = Nurse
        fields = ['name']

class PatientForm(ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Nurse',
            'class': 'form-control'
    }
    ))

    description = forms.CharField(widget = forms.TextInput(attrs =
    {
            'placeholder': "Describe the patient's symptoms",
            'class': 'form-control'
    }
    ))

    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs=
    {
            'class': 'selectpicker',
            'placeholder': 'Select Department', 
    }
    )) 

    class Meta:
        model = Patient
        fields = ['name', 'description', 'department', 'care', 'status']

#Work Related

class WorkShiftForm(ModelForm):
        class Meta:
                model = WorkShift
                fields = '__all__'

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput, label="Email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class DepartmentForm(ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Department',
            'class': 'form-control'
    }
    ))

    description = forms.CharField(widget = forms.TextInput(attrs =
    {
            'placeholder': "Describe the Department",
            'class': 'form-control'
    }
    ))

    class Meta:
        model = Department
        fields = ['name', 'description']