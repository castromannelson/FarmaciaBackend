from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..User.models import UserAccount
from ..Medicine.models import Medicine
from .models import DateBook

class DateBookViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserAccount.objects.create_user(name='TestUser', lastNames = 'TestUser', username='testuser', password='testpassword!23$', rol='Administrador')
        self.client.force_authenticate(user=self.user)

        # Crear un medicamento
        self.medicine_data = {
            'nameMedicine': 'Medicina1',
            'group': 'Grupo1',
            'exist': 0,
            'price': 20.5,
            'state': 'Disponible'
        }
        self.medicine = Medicine.objects.create(**self.medicine_data)

        self.book_data = {
            'medicine': self.medicine,
            'batch': 123,
            'expDate': '2024-12-31',  # Ajusta la fecha de vencimiento según tus necesidades
            'amountBatch': 5
        }
        self.book = DateBook.objects.create(**self.book_data)

    def test_list_books(self):
        response = self.client.get('http://127.0.0.1:8000/DateBook/Books')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(f'http://127.0.0.1:8000/DateBook/Book/{self.book.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['batch'], self.book_data['batch'])

    def test_create_book(self):
        new_book_data = {
            'medicine': self.medicine.nameMedicine,
            'batch': 124,
            'expDate': '2025-01-31',
            'amountBatch': 10
        }
        response = self.client.post('http://127.0.0.1:8000/DateBook/CreateBook', new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DateBook.objects.count(), 2)

    def test_update_book(self):
        updated_data = {
            'medicine': self.medicine.nameMedicine,
            'batch': 125,
            'expDate': '2025-02-28',
            'amountBatch': 15
        }
        response = self.client.put(f'http://127.0.0.1:8000/DateBook/EditBook/{self.book.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.batch, updated_data['batch'])

    def test_delete_book(self):
        response = self.client.delete(f'http://127.0.0.1:8000/DateBook/DeleteBook/{self.book.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DateBook.objects.count(), 0)