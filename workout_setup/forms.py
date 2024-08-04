# forms.py

from django import forms
from .models import WorkoutPlan, Exercise
from django.contrib.auth.models import User

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Name'}),
        }
from django import forms
from .models import WorkoutPlan, Exercise
from django.contrib.auth.models import User

class WorkoutPlanForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False), 
        label="Select Member", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(), 
        label="Select Exercise", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sets = forms.IntegerField(
        min_value=1, 
        label="Sets", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Sets'})
    )
    reps = forms.IntegerField(
        min_value=1, 
        label="Reps", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Reps'})
    )
    day_of_week = forms.ChoiceField(
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday'),
        ], 
        label="Day of Week",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = WorkoutPlan
        fields = ['user', 'exercise', 'sets', 'reps', 'day_of_week']





