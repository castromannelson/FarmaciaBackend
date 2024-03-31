from rest_framework import serializers
from .models import *
from ..Medicine.models import Medicine
#Paciente
class PatientCardSerializer(serializers.ModelSerializer):
    medicine = serializers.CharField(source='medicine.nameMedicine')
    class Meta:
        model = PatientCard
        fields = "__all__"
        
    def create(self, validated_data):
        medicine_name = validated_data.get('medicine')
        if medicine_name:
            medicine = Medicine.objects.get(nameMedicine=medicine_name.get('nameMedicine'))
            validated_data['medicine'] = medicine
        # Crear el paciente
        return PatientCard.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        medicine_name = validated_data.pop('medicine', None)
        if medicine_name:
            medicine = Medicine.objects.get(nameMedicine=medicine_name.get('nameMedicine'))
            instance.medicine = medicine
        
        # Actualizar el resto de los campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Guardar los cambios
        instance.save()
        return instance