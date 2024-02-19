from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# test registration login and logout

class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = {
            "username": "testcase", 
            "email": "test@localhost", 
            "password 1": "some_strong_psw", 
            "password 2": "some_strong_psw"
            }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):
        
        def setUp(self):
            self.user = User.objects.create_user(username="testcase", password="some_strong_psw")
            
        def test_login(self):
            data = {
                "username": "testcase", 
                "password": "some_strong_psw"
                }
            response = self.client.post(reverse('login'), data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
        def test_logout(self):
            self.token = Token.objects.get(user__username="testcase")
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
            response = self.client.post(reverse('logout'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
