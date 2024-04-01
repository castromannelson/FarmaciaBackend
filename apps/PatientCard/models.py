from django.db import models
from ..Medicine.models import Medicine

# Create your models here.
class PatientCard(models.Model):
    namePatient = models.CharField(max_length = 30) # Nombre
    lastNames = models.CharField(max_length = 50) # Apellidos
    age = models.IntegerField(default = 0) # Edad
    ci = models.CharField(max_length = 11, unique=True) # Carnet
    disease = models.CharField(max_length = 30) # Enfermedad
    medicine = models.ForeignKey(Medicine, on_delete = models.DO_NOTHING ,related_name = 'medicine')

    def __str__(self):
        return self.namePatient
