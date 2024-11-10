from django.db import models

# Modelo para almacenar información del paciente
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=30)  # CharField para texto corto
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)  # EmailField es mejor para correos electrónicos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para almacenar información de los test realizados
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=50)
    testname = models.CharField(max_length=100)
    testresult = models.IntegerField() 

    def __str__(self):
        return f"Test {self.testname} - {self.documento}"

# Modelo para almacenar información de los activos/equipos
class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100, unique=True)  # Asegura que el serial sea único
    area = models.CharField(max_length=100, choices=[('Biomédica', 'Biomédica'), ('Infraestructura', 'Infraestructura'), ('Sistemas', 'Sistemas')])
    responsable = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True)  # Campo para almacenar la foto del activo

    def __str__(self):
        return self.nombre
