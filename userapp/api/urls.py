from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework import routers
from .views import registration_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    ]