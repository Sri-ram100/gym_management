from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DietPlanForm, IngredientForm
from .models import DietPlan, Ingredient

@login_required
def create_diet_plan(request):
    if request.method == 'POST':
        form = DietPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_diet_plan')
    else:
        form = DietPlanForm()
    return render(request, 'diet/create_diet_plan.html', {'form': form})

@login_required
def diet_plan_list(request):
    diet_plans = DietPlan.objects.filter(user=request.user)
    return render(request, 'diet/diet_plan_list.html', {'diet_plans': diet_plans})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'diet/ingredient_list.html', {'ingredients': ingredients})

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IngredientForm()
    return render(request, 'diet/ingredient_form.html', {'form': form})
