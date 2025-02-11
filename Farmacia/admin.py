from django.contrib import admin
from .models import EstoqueFarmacia, SaidaEstoque

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['remedio', 'quantidade']
    list_display_links = ['remedio', 'quantidade']

admin.site.register(EstoqueFarmacia, EstoqueAdmin)


class SaidaAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'quantidade', ]
    list_display_links = ['cpf', 'quantidade']

admin.site.register(SaidaEstoque, SaidaAdmin)