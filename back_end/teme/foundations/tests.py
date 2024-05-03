import json

from django.test import TestCase, Client
from django.urls import reverse
from foundations.models import Foundation
from foundations.forms import FoundationForm

class CreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/foundations/create/'

    def test_create_foundation(self):
        data = {'name': 'Test Foundation', 'email': 'test@example.com', 'address': '123 Test St'}
        response = self.client.post(self.url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
        self.assertEqual(response.json()['message'], 'Foundation created successfully')
        self.assertTrue(Foundation.objects.filter(name='Test Foundation').exists())

class ListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/foundations/list/'

    def test_list_foundations(self):
        Foundation.objects.create(name='Test Foundation 1', email='test1@example.com')
        Foundation.objects.create(name='Test Foundation 2', email='test2@example.com')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
        self.assertEqual(len(response.json()['data']), 2)