from django import forms
from .models import *  

class ComputerForm(forms.ModelForm):
    class Meta:
        model = computers
        fields = '__all__'
class ComplaintForm(forms.ModelForm):
    complaint_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Complaint
        fields = ['complaint_details', 'complaint_date']

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['reason', 'repair_date']
        widgets = {
            'repair_date': forms.DateInput(attrs={'type': 'date'})
        }
