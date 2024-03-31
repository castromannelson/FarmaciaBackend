from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Administrador
    path('admin/', admin.site.urls),
    #Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #Aplicaciones
    path('DateBook/', include ('apps.DateBook.urls')),
    path('Doctor/', include ('apps.Doctor.urls')),
    path('Medicine/', include ('apps.Medicine.urls')),
    path('PatientCard/', include ('apps.PatientCard.urls')),
    path('Sale/', include ('apps.Sale.urls')),
    path('User/', include ('apps.User.urls')),
]
