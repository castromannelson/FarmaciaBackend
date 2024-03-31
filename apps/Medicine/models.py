from django.db import models

# Create your models here.

class Medicine(models.Model):
    nameMedicine = models.CharField(max_length = 30, unique = True) #Nombre del Medicamento
    group = models.CharField(max_length = 30,blank = True, default = "" ) # Grupo
    exist = models.IntegerField(default = 0, blank=True) # Existencia
    price = models.FloatField(blank = True, default = 0) # Precio
    
    STATE = [
        ('Disponible','Disponible'),
        ('Agotado', 'Agotado'),
        ('Déficit', 'Déficit'),
        ('Congelado', 'Congelado'),
    ]

    state = models.CharField(max_length = 15, blank = True, default = "Disponible", choices = STATE)
    
    def save(self, *args, **kwargs):
        if self.exist == 0:
            self.state = "Agotado"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nameMedicine
