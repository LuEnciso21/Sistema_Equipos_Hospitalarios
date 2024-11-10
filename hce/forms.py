from django import forms
from .models import Patient, Activo

# Formulario para el modelo Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


# Formulario para ingresar datos del activo
class ActivoForm(forms.ModelForm):
    responsable = forms.ModelChoiceField(
        queryset=Patient.objects.all(), required=True, empty_label=None
    )

    class Meta:
        model = Activo
        fields = ['nombre', 'marca', 'modelo', 'serial', 'area', 'responsable', 'foto']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asignar valores iniciales vacíos si el valor es None
        for field in self.fields:
            if self.fields[field].initial is None:
                self.fields[field].initial = ''

