from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MasterSerializer
from .models import Master

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all().order_by('industry')
    serializer_class = MasterSerializer

# Create your views here.
