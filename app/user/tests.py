from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from app.common.tests import BaseTestCase

User = get_user_model()


class UserTestCase(BaseTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='pass123456',
        )
        self.client.force_authenticate(self.user)

    def test_user_login_register(self):
        user_data = {
            "username": "another",
            "password": "password123",
        }
        login_url = reverse("login")

        response = self.client.post(login_url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ...
