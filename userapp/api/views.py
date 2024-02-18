from rest_framework.decorators import api_view
from userapp.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from userapp import models
from rest_framework import status


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
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response(data=data)