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
    infoPatient = PatientForm(request.POST or None, request.FILES or None)
    success_message = None  # Variable para el mensaje de éxito

    if request.method == 'POST' and infoPatient.is_valid():
        infoPatient.save()
        success_message = "Responsable guardado exitosamente."  # Establecer el mensaje de éxito
        infoPatient = PatientForm()  # Reiniciar el formulario

    return render(request, 'patients/crear.html', {
        'infoPatient': infoPatient,
        'success_message': success_message  # Pasar el mensaje de éxito al template
    })


def borrar(request, id):
    paciente = Patient.objects.get(id=id)
    paciente.delete()
    return redirect('patients')

def editar(request, id):
    paciente = Patient.objects.get(id=id)
    formPatient = PatientForm(request.POST or None, request.FILES or None, instance=paciente)
    success_message = None  # Variable para el mensaje de éxito

    if request.method == 'POST' and formPatient.is_valid():
        formPatient.save()
        success_message = "Responsable editado exitosamente."  # Establecer el mensaje de éxito

    return render(request, 'patients/editar.html', {
        'formPatient': formPatient,
        'success_message': success_message  # Pasar el mensaje de éxito al template
    })

