from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Farmacia.views import EstoqueFarmaciaViewSet, home, estoque_farmacia_lista, SaidaEstoqueViewSet, saidas_estoque_lista, cadastrar_estoque, saida_estoque, salvar_saida_receita


router = DefaultRouter()
router.register(r'farmacia', EstoqueFarmaciaViewSet)
router.register(r'saida', SaidaEstoqueViewSet, basename='saidaestoque')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('Farmacia/estoque', estoque_farmacia_lista, name='estoque farmacia'),
    path('Farmacia/listar_saidas', saidas_estoque_lista, name='lista de todas as saidas do mes'),
    path('Farmacia/cadastrar', cadastrar_estoque, name='cadastrar_estoque'),
    path('saida_estoque/<int:item_id>/', saida_estoque, name='saida_estoque'),
    path('salvar_saida_receita/<int:item_id>/', salvar_saida_receita, name='salvar_saida_receita'),
    path('api/', include(router.urls)),
]