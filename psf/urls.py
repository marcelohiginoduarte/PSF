from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Farmacia.views import EstoqueFarmaciaViewSet, home, estoque_farmacia_lista, SaidaEstoqueViewSet, saidas_estoque_lista


router = DefaultRouter()
router.register(r'farmacia', EstoqueFarmaciaViewSet)
router.register(r'saida', SaidaEstoqueViewSet, basename='saidaestoque')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('Farmacia/estoque', estoque_farmacia_lista, name='estoque farmacia'),
    path('Farmacia/listar_saidas', saidas_estoque_lista, name='lista de todas as saidas do mes '),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
