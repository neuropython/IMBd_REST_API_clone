from rest_framework.decorators import api_view
from userapp.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from userapp import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            
            # ---Token stored in DB---
            token = Token.objects.get(user=account).key
            data['token'] = token
            
            # ---JWT Token---
        
            # token = RefreshToken.for_user(account)
            # data['token'] = {
            #     'refresh': str(token),
            #     'access': str(token.access_token),
            # }
            
        else:
            data = serializer.errors
            
        return Response(data=data, status=status.HTTP_201_CREATED)