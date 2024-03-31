from django.urls import path
from .views import *

urlpatterns = [
    #Pacientes
    path('Patients', PatientCardListView.as_view()),  # Listar
    path('Patient/<id>', PatientCardView.as_view()),  # Obtener
    path('CreatePatient', CreatePatientCardView.as_view()),  # Crear
    path('EditPatient/<int:id>', EditPatientCardView.as_view()),  # Editar
    path('DeletePatient/<int:id>',DeletePatientCardView.as_view()),  # Borrar
]