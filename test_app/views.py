from django.shortcuts import render
from django.http import response, JsonResponse
from rest_framework.views import APIView
from .models import TestModel
from .serializers import SimpleSerializer
from rest_framework import viewsets


class SimpleViewset(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

