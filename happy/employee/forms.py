from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee_profile
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'nrc_no': forms.TextInput(attrs={'class': 'form-control'}),
            'fathername': forms.TextInput(attrs={'class': 'form-control'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'marital': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={"type": "date", 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'entrydate': forms.DateInput(attrs={"type": "date", 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'familytable': forms.FileInput(attrs={'class': 'form-control'}),
            
        }