from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    MEAL_TIMES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.meal_time}"
