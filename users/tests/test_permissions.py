import pytest

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


@pytest.mark.django_db
class UserUnauthorizedTest(APITestCase):
    client = APIClient()

    def test_user_unauthorized(self):
        response = self.client.get('/api/v1/users/', format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_id_unauthorized(self):
        response = self.client.get('/api/v1/users/1/', format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class UserAPIAuthorizationAndPermissionsTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.data = {
            'email': 'email@user.com',
            'first_name': 'Name',
            'last_name': '',
            'password': '+79999999999',
            'phone_number': '+79999999999',
            'is_partner': True,
            'is_student': False,
            'is_teacher': False

        }
        self.login_data = {
            'email': 'email@user.com',
            'password': '+79999999999'
        }

        response = self.client.post('/api/v1/users/', self.data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

        response = self.client.post('/api/v1/jwt/create/', self.login_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.token = response.data['access']

    def test_user_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(self.token))
        response = self.client.get('/api/v1/users/', data={'format': 'json'})
        assert response.status_code, status.HTTP_200_OK == response.content
        assert response.data['count'] == 1

    def test_user_authorized_but_forbidden(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(self.token))
        response = self.client.get('/api/v1/education/lessons/', data={'format': 'json'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
