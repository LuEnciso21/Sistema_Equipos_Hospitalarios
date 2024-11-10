from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, Activo
from .forms import PatientForm, ActivoForm
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages
import os
# Vista de inicio
def inicio(request):
    return render(request, 'pages/index.html')

# Vista de 'About'
def about(request):
    return render(request, 'pages/about.html')

# Vista de consulta
def consultar(request):
    return render(request, 'patients/consultar.html')

# Vista de pacientes
def patients(request):
    paciente = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': paciente})

# Vista para crear un paciente
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

def borrar(request, id, tipo):
    if tipo == 'paciente':
        instance = get_object_or_404(Patient, id=id)
        redirect_url = 'patients'
    elif tipo == 'activo':
        instance = get_object_or_404(Activo, id=id)
        redirect_url = 'equipos'

    instance.delete()
    return redirect(redirect_url)
def editar(request, id):
    instance = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, request.FILES or None, instance=instance)
    template = 'patients/editar.html'
    success_message = "Responsable editado exitosamente."

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, success_message)
        return redirect('consultar')  # Redirige a la URL deseada después de editar

    return render(request, template, {'form': form})
def editar_equipo(request, id):
    instance = get_object_or_404(Activo, id=id)
    form = ActivoForm(request.POST or None, request.FILES or None, instance=instance)
    template = 'patients/editar_equipo.html'  # Cambia a la plantilla adecuada
    success_message = "Equipo editado exitosamente."

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, success_message)
        return redirect('equipos')  # Redirige a la URL deseada después de editar

    return render(request, template, {'form': form})




# Vista para ingresar un activo
def ingresar_activo(request):
    success_message = None  # Variable para el mensaje de éxito

    if request.method == 'POST':
        form = ActivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Activo guardado correctamente"  # Mensaje de éxito
            form = ActivoForm()  # Reiniciar el formulario después de guardar
    else:
        form = ActivoForm()
    
    return render(request, 'patients/ingresar_activo.html', {
        'form': form,
        'success_message': success_message  # Pasar el mensaje de éxito al template
    })
def equipos(request):
    return render(request, 'patients/equipos.html')
def equipos_area(request, area):
    equipos = Activo.objects.filter(area=area)
    equipos_list = []

    for equipo in equipos:
        # Construir la URL completa de la imagen
        foto_url = request.build_absolute_uri(equipo.foto.url) if equipo.foto else None
        equipos_list.append({
            'id': equipo.id,
            'nombre': equipo.nombre,
            'marca': equipo.marca,
            'foto_url': foto_url
        })
    
    data = {'equipos': equipos_list}
    return JsonResponse(data)
def equipo_detalle(request, equipo_id):
    equipo = get_object_or_404(Activo, id=equipo_id)
    return render(request, 'patients/equipo_detalle.html', {'equipo': equipo})