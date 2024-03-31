from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .serializer import *
from .models import *

#Vistas
#Listar
@permission_classes([IsAuthenticated])
class UserListView(APIView):
    def get(self,request):
        users = UserAccount.objects.all()
        
        serializer = UserSerializer(users, many = True)
        
        return Response(serializer.data)
    
#Obtener
@permission_classes([IsAuthenticated])
class UserView(APIView):
    def get(self,request,id):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response({'Error': 'UserAccount not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
#Crear
@permission_classes([IsAuthenticated])
class CreateUserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar
@permission_classes([IsAuthenticated])
class EditUserView(APIView):
    def put(self,request,id):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response({'Error': 'UserAccount not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar
@permission_classes([IsAuthenticated])
class DeleteUserView(APIView):
    def delete(self,request,id):
        try:
            user = UserAccount.objects.get(id=id)
        except UserAccount.DoesNotExist:
            return Response({'Error': 'UserAccount not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)