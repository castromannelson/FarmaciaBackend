from django.urls import path
from .views import *

urlpatterns = [
    #Doctores
    path('Doctors', DoctorsListView.as_view()),  # Listar
    path('Doctor/<id>', DoctorView.as_view()),  # Elemento
    path('CreateDoctor', CreateDoctorView.as_view()),  # Crear
    path('EditDoctor/<int:id>', EditDoctorView.as_view()),  # Editar
    path('DeleteDoctor/<int:id>',DeleteDoctorView.as_view()),  # Borrar
]