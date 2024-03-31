from rest_framework import serializers
from .models import *

#Medicamento
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__" 
