from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Import the custom user model
User = get_user_model()

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create Token for the new user
        Token.objects.create(user=user)
        return user


# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")

        # Generate or retrieve the token
        token, created = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return data
