from rest_framework import serializers
from .models import EstoqueFarmacia

class EstoqueFarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueFarmacia
        fields = '__all__'