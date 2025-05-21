from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def pacientes(request):
    return render(request, 'dashboard/dashboardpac.html')

def pacientesagenda(request):
    return render(request, 'dashboard/agendamentopac.html')

def medicosagenda(request):
    return render(request, 'dashboard/agendamentomed.html')

def medicos(request):
    return render(request, 'dashboard/dashboardmed.html')

