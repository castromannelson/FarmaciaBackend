from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(username=username, password=password, **extra_fields)
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=20) # Nombre
    lastNames  = models.CharField(max_length=40) # Apellidos
    username = models.CharField(max_length=20, unique=True) # Nombre de usuario
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    ROL = [
        ('Administrador','Administrador'),
        ('Dependiente','Dependiente'),
        ('Almacenero','Almacenero'),
    ]
    
    rol = models.CharField(max_length=20, blank = True, default="", choices = ROL)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'lastNames', 'rol']
    
    def __str__(self):
        return self.username