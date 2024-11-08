# measurements/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_measurement/', views.add_measurement, name='add_measurement'),
    path('measurement_list/', views.measurement_list, name='measurement_list'),
    path('delete_measurement/<int:measurement_id>/', views.delete_measurement, name='delete_measurement'),
    path('edit_measurement/<int:measurement_id>/', views.edit_measurement, name='edit_measurement'),
]
