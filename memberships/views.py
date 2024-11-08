from django.http import HttpResponse
from .forms import PlanForm, PaymentForm,PlanSelectionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plan, Payment
from dateutil.relativedelta import relativedelta
from django.utils import timezone

@login_required
def create_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm()
    return render(request, 'memberships/create_plan.html', {'form': form})

@login_required
def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'memberships/plan_list.html', {'plans': plans})

@login_required
def delete_plan(request, plan_id):
    plan = Plan.objects.filter(id=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('plan_list')
    return render(request, 'memberships/plan_list.html', {'plans': Plan.objects.all()})

@login_required
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'memberships/create_payment.html', {'form': form})

@login_required
def select_plan(request):
    if request.method == 'POST':
        form = PlanSelectionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.amount = payment.plan.price
            if not payment.expiry_date:
                payment.expiry_date = payment.start_date + relativedelta(months=payment.plan.duration)
            payment.save()
            return redirect('payment_list_all')
    else:
        form = PlanSelectionForm()
    return render(request, 'memberships/select_plan.html', {'form': form})

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'memberships/payment_list.html', {'payments': payments})

@login_required
def payment_list_all(request):
    payments = Payment.objects.filter()
    return render(request, 'memberships/payment_list_all.html', {'payments': payments})

@login_required
def total_active_members(request):
    today = timezone.now().date()
    active_members_count = Payment.objects.filter(expiry_date__gte=today).count()
    return HttpResponse(f"<script>alert('Total Active Members: {active_members_count}');window.location.replace('/home');</script>")

@login_required
def total_expired_memberships(request):
    today = timezone.now().date()
    expired_memberships_count = Payment.objects.filter(expiry_date__lt=today).count()
    return HttpResponse(f"<script>alert('Total Expired Memberships: {expired_memberships_count}');window.location.replace('/home');</script>")

from datetime import timedelta

@login_required
def members_about_to_expire(request):
    today = timezone.now().date()
    end_date = today + timedelta(days=7)
    expiring_payments = Payment.objects.filter(expiry_date__range=(today, end_date))
    return render(request, 'memberships/members_about_to_expire.html', {'expiring_payments': expiring_payments})


def edit_plan(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_list') 
    else:
        form = PlanForm(instance=plan)
    return render(request, 'memberships/edit_plan.html', {'form': form})
