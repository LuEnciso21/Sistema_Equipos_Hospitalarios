from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=30)  # CharField para texto corto
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)  # EmailField es mejor para correos electrónicos

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=50)
    testname = models.CharField(max_length=100)
    testresult = models.IntegerField() 
    def __str__(self):
        return f"Test {self.testname} - {self.documento}"




