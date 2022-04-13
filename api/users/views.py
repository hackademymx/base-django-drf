from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSignUpSerializer, UserLoginSerializer

# Create your views here.

# Generates tokens manually.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Sign up view.
class UserSignUpView(APIView):
    """
    User signup. Input example:
    {
        "email":"email@email.com",
        "password":"mysuperpassword"
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            data = {
                'msg':'Succesfully registered.  Check your confirmation email.',
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login view.
class UserLoginView(APIView):
    """
    User login.  Input example:
    {
        "email":"email@email.com",
        "password": "mysuperpassword"
    }
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = UserLoginSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.data["email"]
            password = serializer.data["password"]
            
            # Authentication method. If user exists, returns an user instance.
            user = authenticate(email=email, password=password)
            tokens = get_tokens_for_user(user)
            data = {
                'msg':'Successfully logged in.',
                'tokens':tokens
            }

            return Response(data, status=status.HTTP_200_OK)
        except:
            data = {
                'msg':'Must enter valid credentials.'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)