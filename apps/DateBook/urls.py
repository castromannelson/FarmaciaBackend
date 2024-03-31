from django.urls import path
from .views import *

urlpatterns = [
     #Libro
    path('Books', BooksListView.as_view()),  # Listar
    path('Book/<id>', BookView.as_view()),  # Elemento
    path('CreateBook', CreateBookView.as_view()),  # Crear
    path('EditBook/<id>', EditBookView.as_view()),  # Editar
    path('DeleteBook/<id>', DeleteBookView.as_view()),  # Eliminar
]