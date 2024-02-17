from rest_framework.decorators import api_view
from userapp.api.serializers import UserSerializer
from rest_framework.response import Response

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors, status=400)