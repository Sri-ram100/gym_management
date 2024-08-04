from django import forms
from .models import DietPlan, Ingredient
from django.contrib.auth.models import User

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingredient Name'}),
        }

class DietPlanForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False), 
        label="Select Member", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    meal_time = forms.ChoiceField(
        choices=DietPlan.MEAL_TIMES, 
        label="Meal Time", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Ingredients"
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instructions'}),
        label="Instructions"
    )

    class Meta:
        model = DietPlan
        fields = ['user', 'meal_time', 'ingredients', 'instructions']
