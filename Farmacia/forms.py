from django import forms
from .models import EstoqueFarmacia

class EstoqueFarmaciaForm(forms.ModelForm):
    class Meta:
        model = EstoqueFarmacia
        fields = ['remedio', 'quantidade', 'controlado', 'local', 'observacao',]
