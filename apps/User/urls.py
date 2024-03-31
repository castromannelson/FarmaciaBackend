from django.urls import path
from .views import *

urlpatterns = [
    path('Users', UserListView.as_view()), #Listar
    path('User/<int:id>', UserView.as_view()), #Obtener
    path('CreateUser', CreateUserView.as_view()), #Crear
    path('EditUser/<int:id>', EditUserView.as_view()), #Editar
    path('DeleteUser/<int:id>', DeleteUserView.as_view()), #Eliminar
    # path('Login/', LoginUserView.as_view()), # Login
]
