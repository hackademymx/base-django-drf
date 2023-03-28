from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class HomeView(ViewSet):

    def list(self, request):
        message = {
            'message': 'up and runing!'
        }
        return Response(message)
