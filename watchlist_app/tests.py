from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="some_strong_psw")
        self.token = Token.objects.get(user__username="testcase")
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "Best platform",
            "website": "http://www.netflix.com"
        }
        
        response = self.client.post(reverse('stream-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Only admin is allowed to edit the database from that url
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('stream-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="some_strong_psw")
        self.token = Token.objects.get(user__username="testcase")
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_watchlist_create(self):
        data = {
            "name": "New Movie",
            "description": "Story of new movie",
            "active": True
        }
        
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="some_strong_psw")
        self.token = Token.objects.get(user__username="testcase")
        self.watchlist = WatchList.objects.create(
            name="New Movie", 
            description="Story of new movie", 
            active=True,
            time = "2023-11-23T11:11:11Z",
            platform = StreamPlatform.objects.create(
                name="Netflix", 
                about="Best platform", 
                website="http://www.netflix.com")
            )
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_review_create(self):
        data = {
            "review_user": self.user.id,
            "rating": 5,
            "description": "Great Movie",
            "watchlist": self.watchlist
        }
        
        response = self.client.post(reverse('review-create', kwargs={'pk': 1}), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_create_not_allowed(self):
        data = {
            "review_user": self.user.id,
            "rating": 5,
            "description": "Great Movie",
            "watchlist": self.watchlist
        }
        
        response = self.client.post(reverse('review-create', kwargs={'pk': 2}), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)