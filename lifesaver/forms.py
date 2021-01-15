from django import forms
from .models import Doctor, Nurse, Patient
from django.auth.contrib.forms import UserCreationForm

class DoctorForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {

            'placeholder': 'Add a New Doctor',
            'class': 'form-control'
    }
    ))

    department = forms.ModelChoiceField(queryset=department.objects.all)

class NurseForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {
            'placeholder': 'Add a New Nurse',
            'class': 'form-control'
    }
    ))

class PatientForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs = 
    {
        'placeholder': 'Add a New Patient'
        'class': 'form-control'

    
    }))