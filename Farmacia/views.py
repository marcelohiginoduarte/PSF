from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .models import EstoqueFarmacia, SaidaEstoque, SaidaRemediosRecitas
from .serializer import EstoqueFarmaciaSerializer, SaidaEstoqueSerializer
from datetime import datetime
from .forms import EstoqueFarmaciaForm, SaidaEstoqueForm,SaidaRemediosRecitasForm
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')


def estoque_farmacia_lista(request):
    estoque_itens = EstoqueFarmacia.objects.all()
    paginator = Paginator(estoque_itens, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Farmacia_todos_itens.html', {'page_obj': page_obj})


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


def saida_estoque(request, item_id):
    item = get_object_or_404(EstoqueFarmacia, id=item_id)

    if request.method == "POST":
        try:
            quantidade_saida = int(request.POST.get("quantidade", 0))
            quantidade_disponivel = int(item.quantidade)
        except ValueError:
            return HttpResponseBadRequest("Quantidade inválida")

        if quantidade_saida > quantidade_disponivel:
            return HttpResponseBadRequest("Erro: Quantidade de saída maior que a disponível!")

        responsavel_entrega = request.POST.get("responsavel_entrega")
        if not responsavel_entrega:
            return HttpResponseBadRequest("Erro: O responsável pela entrega é obrigatório!")

        saida = SaidaEstoque.objects.create(
            item=item,
            quantidade=quantidade_saida,
            responsavel_recebimento=request.POST.get("responsavel_recebimento"),
            responsavel_entrega=responsavel_entrega,
            cpf=request.POST.get("cpf"),
            sus=request.POST.get("sus"),
            motivo=request.POST.get("motivo"),
            data_saida=timezone.now(),  
        )

        if item.controlado:
            medico_da_receita = request.POST.get("medico_da_receita")
            data_receita = request.POST.get("data_receita")

            if not medico_da_receita or not data_receita:
                return HttpResponseBadRequest("Erro: Medicamentos controlados exigem médico e data da receita!")

            SaidaRemediosRecitas.objects.create(
                item=item,
                medico_da_receita=medico_da_receita,
                data_receita=data_receita,
                responsavel_entrega=responsavel_entrega,
                quantidade=quantidade_saida,
                data_saida=timezone.now(),
            )

        item.quantidade = quantidade_disponivel - quantidade_saida
        item.save()

        messages.success(request, f"Saída de {quantidade_saida} unidades registrada!")
        return redirect("estoque_farmacia")  

    else:
        form = SaidaEstoqueForm()

    return render(request, "Farmacia_modal_saida.html", {"form": form, "item": item})




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

def salvar_saida_receita(request, item_id):
    item = get_object_or_404(EstoqueFarmacia, id=item_id)

    if item.controlado and request.method == 'POST':
        form = SaidaRemediosRecitasForm(request.POST)
        
        if form.is_valid():
            medico_da_receita = form.cleaned_data['medico_da_receita']
            data_receita = form.cleaned_data['data_receita']
            responsacel_entrega = form.cleaned_data['responsacel_entrega']
            quantidade = form.cleaned_data['quantidade']

            SaidaRemediosRecitas.objects.create(
                item=item,
                medico_da_receita=medico_da_receita,
                data_receita=data_receita,
                responsacel_entrega=responsacel_entrega,
                quantidade=quantidade,
                data_saida=timezone.now(),
            )

            item.quantidade -= quantidade
            item.save()

            return redirect("estoque_farmacia")

        else:
            return HttpResponseBadRequest("Formulário inválido")
    
    return render(request, 'modal_receita.html', {'item': item, 'form': form})
