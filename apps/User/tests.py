from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserAccount

class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'John',
            'lastNames': 'Doe',
            'username': 'johndoe',
            'password': 'johndoe!23$',
            'rol': 'Administrador'
        }
        self.user = UserAccount.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)
    
    # Obtener Token        
    def test_jwt_token_generation(self):
        user_data = {
            'username': 'johndoe',
            'password': 'johndoe!23$'
        }
        response = self.client.post('http://127.0.0.1:8000/auth/jwt/create', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    # Listar
    def test_list_users(self):
        response = self.client.get('http://127.0.0.1:8000/User/Users')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Obtener
    def test_retrieve_user(self):
        response = self.client.get(f'http://127.0.0.1:8000/User/User/{self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])

    # Crear
    def test_create_user(self):
        new_user_data = {
            'name': 'Jane',
            'lastNames': 'Smith',
            'username': 'janesmith',
            'password': 'janesmith!23$',
            'rol': 'Dependiente'
        }
        response = self.client.post('http://127.0.0.1:8000/User/CreateUser', new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserAccount.objects.count(), 2)

    # Modificar
    def test_update_user(self):
        updated_data = {
            'name': 'Updated',
            'lastNames': 'UserUpdated',
            'username': 'updateduser',
            'password': 'updatedpassword',
            'rol': 'Almacenero'
        }
        response = self.client.put(f'http://127.0.0.1:8000/User/EditUser/{self.user.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_data['name'])

    # Eliminar
    def test_delete_user(self):
        response = self.client.delete(f'http://127.0.0.1:8000/User/DeleteUser/{self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserAccount.objects.count(), 0)
