from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    ]