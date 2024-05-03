import json 

from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from nonprofits.models import Nonprofit
from django.contrib.auth.models import User
from common import models

class CreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/nonprofits/create/"
        self.user = User.objects.create(username='testing', email='test@gmail.com')
        self.permission = models.Permissions.objects.create(name='create_nonprofit')
        self.user_permissions = models.UserPermissions.objects.create(user=self.user)
        self.user_permissions.permissions.add(self.permission)

    def test_create_nonprofit(self):
        data = {"name": "Test Nonprofit", "email": "test@example.com", "user_name": self.user.username, 'address': 'Hyderabad'}
        response = self.client.post(self.url, data=json.dumps(data), content_type="application/json")
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(response.json()["message"], "Nonprofit created successfully")
        self.assertTrue(Nonprofit.objects.filter(name="Test Nonprofit").exists())

class ListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/nonprofits/list/"

    def test_list_nonprofits(self):
        Nonprofit.objects.create(name="Test Nonprofit 1", email="test1@example.com", address='St 1')
        Nonprofit.objects.create(name="Test Nonprofit 2", email="test2@example.com", address='St 2')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(len(response.json()["data"]), 2)