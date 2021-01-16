from django import forms
from django.forms import ModelForm
from .models import Doctor, Nurse, Patient, Department
from django.contrib.auth.forms import UserCreationForm

class DoctorForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Doctor',
            'class': 'form-control'
    }
    ))

    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs=
    {
            'class': 'selectpicker',
            'placeholder': 'Department', 
    }
    )) 

    class Meta:
        model = Doctor
        fields = ['name', 'department']

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