from django import forms
from .models import *

class ComputerForm(forms.ModelForm):
    class Meta:
        model = computers
        fields = '__all__'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['computer', 'complaint_details', 'complaint_date']
        widgets = {
            'complaint_date': forms.DateInput(attrs={'type': 'date'}),
        }

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['complaint', 'reason', 'repair_date']
        widgets = {
            'repair_date': forms.DateInput(attrs={'type': 'date'}),
        }