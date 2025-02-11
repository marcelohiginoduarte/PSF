from django.db import models

class EstoqueFarmacia(models.Model):
    remedio = models.CharField(max_length=200, blank=False, null=False, unique=True)
    quantidade = models.CharField(max_length=10, blank=False, null=False)
    controlado = models.BooleanField(default=False)
    observacao = models.CharField(max_length=400, blank=True, null=False)


    def __str__(self):
        return self.remedio
