from django.contrib import admin
from .models import Trabalhador, Consulente
from apps.atendimento.admin import AtendimentoPretoVelhoInline

@admin.register(Trabalhador)
class TrabalhadorAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf' )
    list_filter = ()
    list_display = ('nome', 'cpf', 'email', 'telefone',)
    
    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'email',
                'data_nascimento',
                'telefone',
                'cpf',
                'data_ingresso',
                'endereco',
                'cidade',
                'usuario',
                'ativo',
            )
        }),
    )

@admin.register(Consulente)
class ConsulenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'email', 'telefone', 'telefone_whatsapp')

    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'nome',
                'email',
                'data_nascimento',
                'telefone',
                'telefone_whatsapp',
            )
        }),
        ('Outras Informações', {
            'fields': (
                'possui_marcapasso',
                'doencas_preexistentes',
                'descricao_doencas_preexistentes',
                'toma_medicacao',
                'descricao_medicacao',
                'motivo_atendimento'
            )
        }),
        ('', {
            'fields': (
                'usuario',
            )
        }),
    )

    inlines = [
        AtendimentoPretoVelhoInline,
    ]

