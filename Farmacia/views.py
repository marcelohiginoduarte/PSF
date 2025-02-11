from django.shortcuts import render
from rest_framework import viewsets
from .models import EstoqueFarmacia
from .serializer import EstoqueFarmaciaSerializer


def home(request):
    return render(request, 'index.html')

def estoque_farmacia_lista(request):
    estoque_itens = EstoqueFarmacia.objects.all()
    return render(request, 'Farmacia_todos_itens.html', {'estoque_itens':estoque_itens})

class EstoqueFarmaciaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueFarmacia.objects.all()
    serializer_class = EstoqueFarmaciaSerializer