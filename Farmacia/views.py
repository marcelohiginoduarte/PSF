from django.shortcuts import render
from rest_framework import viewsets
from .models import EstoqueFarmacia, SaidaEstoque
from .serializer import EstoqueFarmaciaSerializer, SaidaEstoqueSerializer
from datetime import datetime


def home(request):
    return render(request, 'index.html')

def estoque_farmacia_lista(request):
    estoque_itens = EstoqueFarmacia.objects.all()
    return render(request, 'Farmacia_todos_itens.html', {'estoque_itens':estoque_itens})

class EstoqueFarmaciaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueFarmacia.objects.all()
    serializer_class = EstoqueFarmaciaSerializer

class SaidaEstoqueViewSet(viewsets.ModelViewSet):
    serializer_class = SaidaEstoqueSerializer

    def get_queryset(self):
        mes_atual = datetime.now().month
        ano_atual = datetime.now().year
        return SaidaEstoque.objects.filter(data_saida__month=mes_atual, data_saida__year=ano_atual)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        saida = response.data
        
        item = SaidaEstoque.objects.get(id=saida['id']).item  
        quantidade_saida = saida['quantidade']
        
        estoque_item = EstoqueFarmacia.objects.get(id=item.id)
        
        quantidade_saida = int(quantidade_saida) 
        estoque_item.quantidade = int(estoque_item.quantidade)

        estoque_item.quantidade -= quantidade_saida
        estoque_item.save()
        
        return response
    

def saidas_estoque_lista(request):
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    
    saidas_estoque = SaidaEstoque.objects.filter(data_saida__month=mes_atual, data_saida__year=ano_atual)

    return render(request, 'Farmacia_lista_todas_saidas.html', {'saidas_estoque': saidas_estoque})