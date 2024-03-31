from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..User.models import UserAccount
from .models import Doctor

class DoctorViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserAccount.objects.create_user(name='TestUser', lastNames = 'TestUser', username='testuser', password='testpassword!23$', rol='Administrador')
        self.client.force_authenticate(user=self.user)
        self.doctor_data = {
            'nameDoctor': 'Dr. John',
            'lastNames': 'Doe',
            'folioDoctor': 12345
        }
        self.doctor = Doctor.objects.create(**self.doctor_data)

    # Listar
    def test_list_doctors(self):
        response = self.client.get('http://127.0.0.1:8000/Doctor/Doctors')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one doctor is created in setUp

    # Obtener
    def test_retrieve_doctor(self):
        response = self.client.get(f'http://127.0.0.1:8000/Doctor/Doctor/{self.doctor.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nameDoctor'], self.doctor_data['nameDoctor'])

    # Crear
    def test_create_doctor(self):
        new_doctor_data = {
            'nameDoctor': 'Dr. Jane',
            'lastNames': 'Smith',
            'folioDoctor': 54321
        }
        response = self.client.post('http://127.0.0.1:8000/Doctor/CreateDoctor', new_doctor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)  # Assuming there were no other doctors created before

    # Modificar
    def test_update_doctor(self):
        updated_data = {
            'nameDoctor': 'Dr. Updated',
            'lastNames': 'Updated',
            'folioDoctor': 67890
        }
        response = self.client.put(f'http://127.0.0.1:8000/Doctor/EditDoctor/{self.doctor.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.doctor.refresh_from_db()
        self.assertEqual(self.doctor.nameDoctor, updated_data['nameDoctor'])

    # Eliminar
    def test_delete_doctor(self):
        response = self.client.delete(f'http://127.0.0.1:8000/Doctor/DeleteDoctor/{self.doctor.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctor.objects.count(), 0)
