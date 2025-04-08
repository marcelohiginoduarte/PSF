from django import forms
from .models import EstoqueFarmacia, SaidaEstoque, SaidaRemediosRecitas

class EstoqueFarmaciaForm(forms.ModelForm):
    class Meta:
        model = EstoqueFarmacia
        fields = ['remedio', 'quantidade', 'controlado', 'local', 'observacao',]


class SaidaEstoqueForm(forms.ModelForm):
    class Meta:
        model = SaidaEstoque
        fields = ['quantidade', 'responsavel_recebimento', 'responsavel_entrega', 'cpf', 'sus', 'motivo']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'responsavel_recebimento': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'sus': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SaidaRemediosRecitasForm(forms.ModelForm):
    class Meta:
        model = SaidaRemediosRecitas
        fields = ['medico_da_receita', 'data_receita', 'responsavel_entrega', 'quantidade']

    data_receita = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2100)))
