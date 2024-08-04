from django import forms
from .models import Plan, Payment
from django.contrib.auth.models import User

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'price', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plan Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Plan Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in Months'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'plan', 'amount', 'expiry_date']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Expiry Date'}),
        }

class PlanSelectionForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False), label="Select Member", widget=forms.Select(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    expiry_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Payment
        fields = ['user', 'plan', 'start_date', 'expiry_date']
        widgets = {
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Start Date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Expiry Date'}),
        }
