from rest_framework import serializers
from .models import EstoqueFarmacia, SaidaEstoque

class EstoqueFarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueFarmacia
        fields = '__all__'


class SaidaEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaidaEstoque
        fields = '__all__'