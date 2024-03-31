from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..User.models import UserAccount
from ..Medicine.models import Medicine
from ..DateBook.models import DateBook
from .models import Sale

class SaleViewsTestCase(TestCase):
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

        # Crear un lote
        self.batch_data = {
            'medicine': self.medicine,
            'batch': 123,
            'expDate': '2024-12-31',
            'amountBatch': 10
        }
        self.batch = DateBook.objects.create(**self.batch_data)

        self.sale_data = {
            'medicine': self.medicine,
            'amount': 5,
            'batch': self.batch,
            'profit': 5 * 20.5  # Cantidad * Precio
        }
        self.sale = Sale.objects.create(**self.sale_data)

    def test_list_sales(self):
        response = self.client.get('http://127.0.0.1:8000/Sale/Sales')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_filtered_sales(self):
        response = self.client.get('http://127.0.0.1:8000/Sale/SalesFilter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_sale(self):
        response = self.client.get(f'http://127.0.0.1:8000/Sale/Sale/{self.sale.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], self.sale_data['amount'])

    def test_create_sale(self):
        new_sale_data = {
            'medicine': self.medicine.nameMedicine,
            'amount': 3,
            'batch': self.batch.batch,
            'profit': 3 * 20.5
        }
        response = self.client.post('http://127.0.0.1:8000/Sale/CreateSale', new_sale_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sale.objects.count(), 2)

    def test_update_sale(self):
        updated_data = {
            'medicine': self.medicine.nameMedicine,
            'amount': 6,
            'batch': self.batch.batch,
            'profit': 6 * 20.5
        }
        response = self.client.put(f'http://127.0.0.1:8000/Sale/EditSale/{self.sale.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sale.refresh_from_db()
        self.assertEqual(self.sale.amount, updated_data['amount'])

    def test_delete_sale(self):
        response = self.client.delete(f'http://127.0.0.1:8000/Sale/DeleteSale/{self.sale.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sale.objects.count(), 0)
