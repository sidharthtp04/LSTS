from django import forms
from .models import *



class ComputerForm(forms.ModelForm):
    class Meta:
        model = computers
        fields= '__all__'
