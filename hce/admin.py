from django.contrib import admin
from .models import Patient, Test

# Register your models here.
admin.site.register(Patient)
admin.site.register(Test)