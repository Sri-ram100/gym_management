from django.urls import path
from . import views

urlpatterns = [
    path('create_diet_plan/', views.create_diet_plan, name='create_diet_plan'),
    path('diet_plan_list/', views.diet_plan_list, name='diet_plan_list'),
    path('ingredient_list/', views.ingredient_list, name='ingredient_list'),
    path('ingredient_create/', views.ingredient_create, name='ingredient_create'),
]
