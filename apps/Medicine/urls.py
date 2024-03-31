from django.urls import path
from .views import *

urlpatterns = [
     #Medicamentos
    path('Medicines', MedicinesListView.as_view()),  # Listar
    path('Medicine/<id>', MedicineView.as_view()),  # Elemento
    path('CreateMedicine', CreateMedicineView.as_view()),  # Crear
    path('EditMedicine/<id>', EditMedicineView.as_view()),  # Editar
    path('DeleteMedicine/<id>', DeleteMedicineView.as_view()),  # Eliminar
    path('ReporteMedicineExel', ReporteMedicineExel.as_view()), # Reporte de Medicamentos
]