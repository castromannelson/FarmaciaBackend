from rest_framework import serializers
from .models import *
from ..Medicine.models import Medicine

#LibroVenc
class DateBookSerializer(serializers.ModelSerializer):
    medicine = serializers.CharField(source='medicine.nameMedicine')
    class Meta:
        model = DateBook
        fields = "__all__"

    def create(self, validated_data):
        medicine_name = validated_data.get('medicine')
        if medicine_name:
            medicine = Medicine.objects.get(nameMedicine=medicine_name.get('nameMedicine'))
            validated_data['medicine'] = medicine
        # Crear el paciente
        return DateBook.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        medicine_name = validated_data.pop('medicine', None)
        if medicine_name:
            medicine = Medicine.objects.get(nameMedicine=medicine_name.get('nameMedicine'))
            medicine.exist -= instance.amountBatch
            instance.medicine = medicine
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance