from django.shortcuts import render
from rest_framework import viewsets
from .models import EstoqueFarmacia
from .serializer import EstoqueFarmaciaSerializer

class EstoqueFarmaciaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueFarmacia.objects.all()
    serializer_class = EstoqueFarmaciaSerializer