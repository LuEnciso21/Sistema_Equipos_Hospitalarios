from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm


# Create your views here.

def inicio(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def consultar(request):
    return render(request, 'patients/consultar.html')

def patients(request):
    paciente = Patient.objects.all()
    return render(request , 'patients/index.html', {'patients':paciente})

def crear(request):
    infoPatient = PatientForm(request.POST or None , request.FILES or None)
    if infoPatient.is_valid():
        infoPatient.save()
        return redirect('patients')
    return render(request, 'patients/crear.html')

def borrar(request, id):
    paciente = Patient.objects.get(id=id)
    paciente.delete()
    return redirect('patients')

def editar(request, id):
    paciente = Patient.objects.get(id=id)
    formPatient = PatientForm(request.POST or None, request.FILES or None, instance=paciente)
    if formPatient.is_valid() and request.method == 'POST':
        formPatient.save()
        return redirect('patients')
    return render(request, 'patients/editar.html' , {'formPatient':formPatient})
