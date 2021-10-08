from django.contrib import admin
from .models import Atendimento, Consulente

class AtendimentoInline(admin.StackedInline):
    model = Atendimento
    extra = 1

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    search_fields = ()
    list_filter = ('data', 'precisa_retorno')
    list_display = ('consulente', 'data')

    fieldsets = (
        (None, {
            'fields': (
                'consulente',
                'data',
                'precisa_retorno',
                'recomendacoes',
            )
        }),
    )

@admin.register(Consulente)
class ConsulenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'email', 'telefone', 'telefone_whatsapp')

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'data_nascimento',
                'email',
                'telefone',
                'telefone_whatsapp',
                'possui_marcapasso',
                'doencas_preexistentes',
                'descricao_doencas_preexistentes',
                'toma_medicacao',
                'descricao_medicacao',
                'motivo_atendimento'
            )
        }),
    )

    inlines = [
        AtendimentoInline,
    ]

