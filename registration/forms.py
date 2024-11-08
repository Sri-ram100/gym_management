from django import forms
from .models import Registers, Trainers
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registers
        fields = [
            'first_name',
            'last_name',
            'sex',
            'age',
            'email',
            'mobile_number',
            'address',
            'join_date'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address'}),
            'join_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Join Date'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = [
            'first_name',
            'last_name',
            'sex',
            'age',
            'email',
            
            'mobile_number',
            'hire_date'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'hire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Hire Date'}),
        }
