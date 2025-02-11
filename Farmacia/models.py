from django.db import models

class EstoqueFarmacia(models.Model):
    locais=[
        ('jardim3', 'Jardim Neopolis 3')
    ]

    remedio = models.CharField(max_length=200, blank=False, null=False, unique=True)
    quantidade = models.CharField(max_length=10, blank=False, null=False)
    controlado = models.BooleanField(default=False)
    local = models.CharField(max_length=50, choices=locais,)
    observacao = models.CharField(max_length=400, blank=True, null=False)


    def __str__(self):
        return self.remedio


class SaidaEstoque(models.Model):
    item = models.ForeignKey(EstoqueFarmacia, on_delete=models.CASCADE)
    responsavel_recebimento = models.CharField(max_length=150, null=True, blank=True)
    responsacel_entrega = models.CharField(max_length=150, null=True, blank=True)
    quantidade = models.IntegerField()
    data_saida = models.DateField()
    cpf = models.CharField(max_length=15, blank=False, null=False)
    sus = models.CharField(max_length=15, blank=False, null=False)
    motivo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.quantidade} de {self.item.remedio} - {self.data_saida}"

    class Meta:
        ordering = ['-data_saida']