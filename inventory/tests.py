from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Item

class InventoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.item_data = {'name': 'Test Item', 'description': 'Test Description'}
        self.item = Item.objects.create(**self.item_data)
    
    def test_create_item(self):
        response = self.client.post(reverse('item-list'), self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        response = self.client.get(reverse('item-detail', kwargs={'item_id': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_item(self):
        update_data = {'name': 'Updated Item', 'description': 'Updated Description'}
        response = self.client.put(reverse('item-detail', kwargs={'item_id': self.item.id}), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_item(self):
        response = self.client.delete(reverse('item-detail', kwargs={'item_id': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
