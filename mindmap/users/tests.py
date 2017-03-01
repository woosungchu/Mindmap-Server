from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt import utils
from django.contrib.auth.models import User
import json

"""
#status code
http://www.django-rest-framework.org/api-guide/status-codes/

#url namespaces
http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
"""

class UsersApiTest(APITestCase):
    def test_postUser(self):
        """
        - positive http status
        - token should not contain password
        """
        url = reverse('api-user:user-list')
        data = {
            'username': 'testuser',
            "email": "test@testuser.com",
            'password': 'testuser'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse('password' in response.data)

class UsersJwtTest(APITestCase):
    """
    Focus on..
    - JWT
    - Security
    """

    def setUp(self):
        self.username = "woosungchu"
        self.password = "secret_password"
        self.email = "test@testuser.com"
        self.user = User.objects.create_user(self.username,self.email,self.password)
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_login(self):
        """
        send access token if valid
        """
        url = reverse('login')
        response = self.client.post(url, self.data, format='json')

        decoded_payload = utils.jwt_decode_handler(response.data['token'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_payload['username'], self.username)
        self.assertFalse('password' in decoded_payload)

    def test_invalidLogin(self):
        """
        send negative http status to invalid login
        """
        url = reverse('jwt-refresh')
        data = {
            'username': 'babo',
            'password': 'babo'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_expired_token(self):
        """
        block expired token
        """
        payload = utils.jwt_payload_handler(self.user)
        payload['exp'] = 1
        token = utils.jwt_encode_handler(payload)

        auth = 'JWT {0}'.format(token)
        url = reverse('login')
        client = APIClient(enforce_csrf_checks=True)
        response = client.post(url, self.data, HTTP_AUTHORIZATION=auth, format='json')

        decoded_payload = utils.jwt_decode_handler(response.data['token'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertFalse('password' in decoded_payload)
        self.assertEqual(decoded_payload['username'], self.username)
