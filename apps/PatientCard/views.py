from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from .models import *


# Create your views here.
#Listar
@permission_classes([IsAuthenticated])
class PatientCardListView(APIView):
    def get(self,request):
        patients = PatientCard.objects.all()
        
        serializer = PatientCardSerializer(patients, many = True)
        
        return Response(serializer.data)

#Obtener
@permission_classes([IsAuthenticated])
class PatientCardView(APIView):
    def get(self,request,id):
        try:
            patient = PatientCard.objects.get(id=id)
        except PatientCard.DoesNotExist:
            return Response({'Error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientCardSerializer(patient)
        return Response(serializer.data)
        
#Crear
@permission_classes([IsAuthenticated])
class CreatePatientCardView(APIView):
   def post(self,request):
        serializer = PatientCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar
@permission_classes([IsAuthenticated])
class EditPatientCardView(APIView):
    def put(self,request,id):
        try:
            patient = PatientCard.objects.get(id=id)
        except PatientCardSerializer.DoesNotExist:
            return Response({'Error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientCardSerializer(patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Eliminar
@permission_classes([IsAuthenticated])
class DeletePatientCardView(APIView):
    def delete(self,request,id):
        try:
            patient = PatientCard.objects.get(id=id)
        except PatientCard.DoesNotExist:
            return Response({'Error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)