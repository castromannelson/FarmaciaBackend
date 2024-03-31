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
class BooksListView(APIView):
    def get(self,request):
        books = DateBook.objects.all()
        
        serializer = DateBookSerializer(books, many = True)
        
        return Response(serializer.data)

#Obtener
@permission_classes([IsAuthenticated])
class BookView(APIView):
    def get(self,request,id):
        try:
            book = DateBook.objects.get(id=id)
        except DateBook.DoesNotExist:
            return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DateBookSerializer(book)
        return Response(serializer.data)

#Crear
@permission_classes([IsAuthenticated])
class CreateBookView(APIView):
    def post(self,request):
        serializer = DateBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Editar
@permission_classes([IsAuthenticated])
class EditBookView(APIView):
    def put(self,request,id):
        try:
            book = DateBook.objects.get(id=id)
        except DateBook.DoesNotExist:
            return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DateBookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Eliminar
@permission_classes([IsAuthenticated])
class DeleteBookView(APIView):
    def delete(self,request,id):
        try:
            book = DateBook.objects.get(id=id)
        except DateBook.DoesNotExist:
            return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
