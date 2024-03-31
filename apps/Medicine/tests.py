from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..User.models import UserAccount
from .models import Medicine

class MedicineViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserAccount.objects.create_user(name='TestUser', lastNames = 'TestUser', username='testuser', password='testpassword!23$', rol='Administrador')
        self.client.force_authenticate(user=self.user)
        self.medicine_data = {
            'nameMedicine': 'Medicina1',
            'group': 'Grupo1',
            'exist': 10,
            'price': 20.5,
            'state': 'Disponible'
        }
        self.medicine = Medicine.objects.create(**self.medicine_data)

    def test_list_medicines(self):
        response = self.client.get('http://127.0.0.1:8000/Medicine/Medicines')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_medicine(self):
        response = self.client.get(f'http://127.0.0.1:8000/Medicine/Medicine/{self.medicine.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nameMedicine'], self.medicine_data['nameMedicine'])

    def test_create_medicine(self):
        new_medicine_data = {
            'nameMedicine': 'Medicina2',
            'group': 'Grupo2',
            'exist': 5,
            'price': 15.75,
            'state': 'Disponible'
        }
        response = self.client.post('http://127.0.0.1:8000/Medicine/CreateMedicine', new_medicine_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Medicine.objects.count(), 2)

    def test_update_medicine(self):
        updated_data = {
            'nameMedicine': 'UpdatedMedicina',
            'group': 'UpdatedGrupo',
            'exist': 15,
            'price': 25.5,
            'state': 'Congelado'
        }
        response = self.client.put(f'http://127.0.0.1:8000/Medicine/EditMedicine/{self.medicine.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.medicine.refresh_from_db()
        self.assertEqual(self.medicine.nameMedicine, updated_data['nameMedicine'])

    def test_delete_medicine(self):
        response = self.client.delete(f'http://127.0.0.1:8000/Medicine/DeleteMedicine/{self.medicine.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Medicine.objects.count(), 0)

    def test_reporte_medicamentos_excel(self):
        response = self.client.get('http://127.0.0.1:8000/Medicine/ReporteMedicineExel')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get('Content-Disposition'), 'attachment; filename=ReporteMedicamentosExel.xlsx')
