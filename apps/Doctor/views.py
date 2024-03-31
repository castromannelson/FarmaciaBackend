# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import *
from .models import *

# Create your views here.
#Listar
@permission_classes([IsAuthenticated])
class DoctorsListView(APIView):
    def get(self,request):
        doctors = Doctor.objects.all()
        
        serializer = DoctorSerializer(doctors, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

#Obtener
@permission_classes([IsAuthenticated])
class DoctorView(APIView):
    def get(self,request,id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'Error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear
@permission_classes([IsAuthenticated])
class CreateDoctorView(APIView):
    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar
@permission_classes([IsAuthenticated])
class EditDoctorView(APIView):
    def put(self,request,id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'Error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Eliminar
@permission_classes([IsAuthenticated])
class DeleteDoctorView(APIView):
    def delete(self,request,id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'Error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)