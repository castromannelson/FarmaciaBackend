# from collections.abc import Iterable
from django.db import models
from apps.Medicine.models import Medicine
from django.utils import timezone

# Create your models here.
class DateBook(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.DO_NOTHING) #Medicamento
    batch = models.IntegerField(default = 0, null = True) #Lote
    expDate = models.DateField(default = timezone.now) #Fecha vencimiento
    amountBatch = models.IntegerField(default = 0) #Cantidad del Lote
    
    def save(self, *args, **kargs):
        if self.medicine.exist == 0 and self.amountBatch > 0:     
            self.medicine.state = "Disponible"
            
        #Actualiza la existencia del medicamento
        self.medicine.exist += self.amountBatch
        
        self.medicine.save()
        
        super().save(*args, **kargs)
        
    def delete(self, *args, **kwargs):
        # Resta la cantidad eliminada de existencia del medicamento
        self.medicine.exist -= self.amountBatch
        
        self.medicine.save()
        super().delete(*args, **kwargs)

    def __srt__(self):
        return f"{self.medicine}-{self.batch}"