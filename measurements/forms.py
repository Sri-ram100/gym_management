from django import forms
from .models import Measurements

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ['height', 'weight', 'bicep', 'forearm', 'shoulder', 'chest', 'waist', 'thigh', 'calf', 'bmi', 'date_recorded']
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_height'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_weight'}),
            'bicep': forms.NumberInput(attrs={'class': 'form-control'}),
            'forearm': forms.NumberInput(attrs={'class': 'form-control'}),
            'shoulder': forms.NumberInput(attrs={'class': 'form-control'}),
            'chest': forms.NumberInput(attrs={'class': 'form-control'}),
            'waist': forms.NumberInput(attrs={'class': 'form-control'}),
            'thigh': forms.NumberInput(attrs={'class': 'form-control'}),
            'calf': forms.NumberInput(attrs={'class': 'form-control'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_bmi', 'readonly': 'readonly'}),
            'date_recorded': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
