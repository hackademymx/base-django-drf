from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

class UserSignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'is_active',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate(self, attrs):
        password = attrs["password"]

        # Validates password length parameters.
        if len(password) < 6 or len(password) > 20:
            raise serializers.ValidationError('Password must have unless 6 characters long and no more than 20.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
