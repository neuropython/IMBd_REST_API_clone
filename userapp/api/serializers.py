from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        try:
            password = self.validated_data['password']
            password2 = self.validated_data['password2']
            email = self.validated_data['email']
            username = self.validated_data['username']
        except KeyError as e:
            raise serializers.ValidationError(f'Missing required key: {e}')
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        if User.objects.filter(email=self.validated_data.get('email')).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})
        
        user = User.objects.create_user( 
        email=email,
        password=password,
        username=username
        )
        user.save()
        return user
        
    