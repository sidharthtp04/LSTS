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
class ComplaintFilterForm(forms.Form):
    c_label = forms.ModelChoiceField(queryset=computers.objects.all(), required=False, label='Computer Label')
    lab_name = forms.ModelChoiceField(queryset=lab.objects.all(), required=False, label='Lab Name')