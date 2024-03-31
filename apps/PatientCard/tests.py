from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..User.models import UserAccount
from ..Medicine.models import Medicine
from .models import PatientCard

class PatientCardViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserAccount.objects.create_user(name='TestUser', lastNames = 'TestUser', username='testuser', password='testpassword!23$', rol='Administrador')
        self.client.force_authenticate(user=self.user)
        
        # Crear un medicamento
        self.medicine_data = {
            'nameMedicine': 'Medicina1',
            'group': 'Grupo1',
            'exist': 10,
            'price': 20.5,
            'state': 'Disponible'
        }
        self.medicine = Medicine.objects.create(**self.medicine_data)
        
        self.patient_data = {
            'namePatient': 'John',
            'lastNames': 'Doe',
            'age': 30,
            'ci': '12345678901',
            'disease': 'Covid-19',
            'medicine': self.medicine
        }
        self.patient = PatientCard.objects.create(**self.patient_data)

    def test_list_patients(self):
        response = self.client.get('http://127.0.0.1:8000/PatientCard/Patients')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_patient(self):
        response = self.client.get(f'http://127.0.0.1:8000/PatientCard/Patient/{self.patient.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['namePatient'], self.patient_data['namePatient'])

    def test_create_patient(self):
        self.medicine_data = {
            'nameMedicine': 'Medicina2',
            'group': 'Grupo2',
            'exist': 15,
            'price': 26.5,
            'state': 'Disponible'
        }
        self.medicine = Medicine.objects.create(**self.medicine_data)
        
        new_patient_data = {
            'namePatient': 'Jane',
            'lastNames': 'Smith',
            'age': 25,
            'ci': '98765432101',
            'disease': 'Influenza',
            'medicine': 'Medicina2'
        }
        response = self.client.post('http://127.0.0.1:8000/PatientCard/CreatePatient', new_patient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PatientCard.objects.count(), 2)

    def test_update_patient(self):
        self.medicine_data = {
            'nameMedicine': 'Medicina3',
            'group': 'Grupo3',
            'exist': 20,
            'price': 30.9,
            'state': 'Disponible'
        }
        self.medicine = Medicine.objects.create(**self.medicine_data)
        
        updated_data = {
            'namePatient': 'UpdatedPatient',
            'lastNames': 'UpdatedLastNames',
            'age': 40,
            'ci': '11111111111',
            'disease': 'UpdatedDisease',
            'medicine': 'Medicina3'
        }
        response = self.client.put(f'http://127.0.0.1:8000/PatientCard/EditPatient/{self.patient.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.namePatient, updated_data['namePatient'])

    def test_delete_patient(self):
        response = self.client.delete(f'http://127.0.0.1:8000/PatientCard/DeletePatient/{self.patient.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PatientCard.objects.count(), 0)
