from datetime import datetime
from django.utils import timezone
from django.db import models
from apps.Medicine.models import Medicine
from apps.DateBook.models import DateBook


# Create your models here.
class Sale(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.DO_NOTHING) # Medicamento
    amount = models.IntegerField(default = 0) # Cantidad
    saleDate = models.DateField(default=timezone.now) # Fecha en que se realizo la venta
    batch = models.ForeignKey(DateBook, on_delete = models.DO_NOTHING, null = True) # Lote
    profit = models.FloatField(default = 0, blank=True, null=True, editable=False) # Importe o Ganancia


    def save(self, *args, **kargs ):
        #Actualiza la existencia del medicamento al crear una venta
        self.medicine.exist -= self.amount
        self.medicine.exist -= (self.batch.amountBatch - self.amount)
        
        #Calcula el importe
        self.profit = self.amount * self.medicine.price
        
        #Actualiza la cantidad restante del lote
        self.batch.amountBatch -= self.amount

        if isinstance(self.saleDate, datetime):
            self.saleDate = self.saleDate.date()
        
        self.medicine.save()
        self.batch.save()
        super().save(*args, **kargs)

    def __str__(self):
        return f"{self.medicine}-{self.saleDate}"