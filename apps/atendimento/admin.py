from django.contrib import admin
from .models import AtendimentoPretoVelho

class AtendimentoPretoVelhoInline(admin.StackedInline):
    model = AtendimentoPretoVelho
    extra = 1

@admin.register(AtendimentoPretoVelho)
class AtendimentoPretoVelhoAdmin(admin.ModelAdmin):
    search_fields = ()
    list_filter = ('data', 'precisa_retorno', 'status')
    list_display = ('data', 'consulente', 'status')

    fieldsets = (
        (None, {
            'fields': (
                'consulente',
                'medium',
                'guia',
                'mediador',
                'data',
                'status',
                'precisa_retorno',
                'recomendacoes',
            )
        }),
    )
