from django.shortcuts import render, redirect
from .forms import MeasurementsForm
from .models import Measurements
from django.contrib.auth.decorators import login_required

@login_required
def add_measurement(request):
    if request.method == 'POST':
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user  
            measurement.save()
            return redirect('measurement_list')
    else:
        form = MeasurementsForm()
    return render(request, 'measurements/add_measurement.html', {'form': form})

@login_required
def measurement_list(request):
    measurements = Measurements.objects.filter(user=request.user)
    return render(request, 'measurements/measurement_list.html', {'measurements': measurements})


def delete_measurement(request, measurement_id):
    measurement = Measurements.objects.filter(id=measurement_id)
    measurement.delete()
    return redirect('measurement_list') 

@login_required
def edit_measurement(request, measurement_id):
    measurement = Measurements.objects.filter(id=measurement_id)

    if request.method == 'POST':
        form = MeasurementsForm(request.POST, instance=measurement)
        if form.is_valid():
            form.save()
            return redirect('measurement_list')
    else:
        form = MeasurementsForm(instance=measurement)
    return render(request, 'measurements/edit_measurement.html', {'form': form})
