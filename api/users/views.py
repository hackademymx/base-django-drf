from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSignUpSerializer
from users.models import User

# Create your views here.

class UserSignUpView(APIView):
    """
    User signup. Input example:
    {
        "email":"email@email.com",
        "password":"mysuperpassword"
    }
    """

    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)