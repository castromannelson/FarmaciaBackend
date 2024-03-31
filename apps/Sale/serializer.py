from rest_framework import serializers
from .models import *

#Venta
class SaleSerializer(serializers.ModelSerializer):
    medicine = serializers.CharField(source='medicine.nameMedicine') # Medicamento
    batch = serializers.IntegerField(source='batch.batch') # Lote
    class Meta:
        model = Sale
        fields = "__all__"
        
    def create(self, validated_data):
        batch = validated_data.pop('batch', None)
        medicine_name = validated_data.pop('medicine', None)
        
        medicine = Medicine.objects.get(nameMedicine=medicine_name.get('nameMedicine'))
        dateBook = DateBook.objects.get(batch=batch.get('batch'), medicine=medicine.id)

        validated_data['medicine'] = medicine
        validated_data['batch'] = dateBook
            
        return Sale.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        medicine_data = validated_data.pop('medicine', None)
        batch_data = validated_data.pop('batch', None)
        
        if medicine_data:
            instance.medicine = Medicine.objects.get(nameMedicine=medicine_data.get('nameMedicine'))

        if batch_data:
            instance.batch = DateBook.objects.get(batch=batch_data.get('batch'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance