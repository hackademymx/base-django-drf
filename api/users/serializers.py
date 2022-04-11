from rest_framework import serializers
from users.models import User

class UserSignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'email',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user