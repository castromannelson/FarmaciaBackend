from django.urls import path
from .views import *

urlpatterns = [
    # Ventas
    path('Sales', SalesListView.as_view()),  # Listar
    path('SalesFilter', SalesFilterListView.as_view()), # Lista Filtrada por las ventas de la ultima semana
    path('Sale/<id>', SaleView.as_view()),  # Elemento
    path('CreateSale', CreateSaleView.as_view()),  # Crear
    path('EditSale/<id>', EditSaleView.as_view()),  #Editar
    path('DeleteSale/<id>', DeleteSaleView.as_view()), #Eliminar
    path('ReporteSaleExel', ReporteSaleExel.as_view()), # Reporte de Ventas
]