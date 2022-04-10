import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class WeatherTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='usertest',
            password='passwordtest'
        )
        self.client.login(username='usertest', password='passwordtest')
    
    def test_users_authenticated(self):
        response = self.client.get(reverse('weather', kwargs={'city': 'santiago', 'country': 'cl'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_users_no_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('weather', kwargs={'city': 'santiago', 'country': 'cl'}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)