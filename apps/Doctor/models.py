from django.db import models

# Create your models here.
class Doctor(models.Model):
    nameDoctor = models.CharField(max_length = 30) # Nombre
    lastNames = models.CharField(max_length = 100) # Apellidos
    folioDoctor = models.IntegerField( default = 0, unique=True) # Folio

    def __str__(self):
        return self.nameDoctor