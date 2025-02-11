from django import forms
from .models import EstoqueFarmacia, SaidaEstoque

class EstoqueFarmaciaForm(forms.ModelForm):
    class Meta:
        model = EstoqueFarmacia
        fields = ['remedio', 'quantidade', 'controlado', 'local', 'observacao',]


class SaidaEstoqueForm(forms.ModelForm):
    class Meta:
        model = SaidaEstoque
        fields = ['quantidade', 'responsavel_recebimento', 'responsacel_entrega', 'cpf', 'sus', 'motivo']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'responsavel_recebimento': forms.TextInput(attrs={'class': 'form-control'}),
            'responsacel_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'sus': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
