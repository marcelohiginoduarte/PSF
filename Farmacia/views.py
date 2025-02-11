from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import EstoqueFarmacia, SaidaEstoque
from .serializer import EstoqueFarmaciaSerializer, SaidaEstoqueSerializer
from datetime import datetime
from .forms import EstoqueFarmaciaForm


def home(request):
    return render(request, 'index.html')

def estoque_farmacia_lista(request):
    estoque_itens = EstoqueFarmacia.objects.all()
    return render(request, 'Farmacia_todos_itens.html', {'estoque_itens':estoque_itens})

class EstoqueFarmaciaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueFarmacia.objects.all()
    serializer_class = EstoqueFarmaciaSerializer


def cadastrar_estoque(request):
    if request.method == "POST":
        form = EstoqueFarmaciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque farmacia')
    else:
        form = EstoqueFarmaciaForm()

    return render(request, 'Farmacia_entrada.html', {'form': form})


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
    mes = int(request.GET.get('mes', datetime.now().month))
    ano = int(request.GET.get('ano', datetime.now().year))

    saidas_estoque = SaidaEstoque.objects.filter(data_saida__month=mes, data_saida__year=ano)

    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    return render(request, 'Farmacia_lista_todas_saidas.html', {
        'saidas_estoque': saidas_estoque,
        'mes': mes,
        'ano': ano,
        'meses': meses
    })
