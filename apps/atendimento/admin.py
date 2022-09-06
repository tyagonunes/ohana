from django.contrib import admin
from .models import AtendimentoPretoVelho, AtendimentoPretoVelhoTerapia, AtendimentoPretoVelhoBanho

class AtendimentoPretoVelhoInline(admin.StackedInline):
    model = AtendimentoPretoVelho
    extra = 1

class AtendimentoPretoVelhoTerapiaInline(admin.StackedInline):
    model = AtendimentoPretoVelhoTerapia
    extra = 1

class AtendimentoPretoVelhoBanhoInline(admin.StackedInline):
    model = AtendimentoPretoVelhoBanho
    extra = 1
@admin.register(AtendimentoPretoVelho)
class AtendimentoPretoVelhoAdmin(admin.ModelAdmin):
    search_fields = ()
    list_filter = ('data', 'precisa_retorno', 'status')
    list_display = ('data', 'consulente', 'status')

    inlines = [
        AtendimentoPretoVelhoTerapiaInline,
        AtendimentoPretoVelhoBanhoInline
    ]

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
