from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your models here.

class AccountAPIView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response('BANK ACCOUNT.', status=status.HTTP_200_OK)