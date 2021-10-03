from django.contrib import admin
from .models import ConsultaPretosVelhos


@admin.register(ConsultaPretosVelhos)
class ConsultaPretosVelhosAdmin(admin.ModelAdmin):
    search_fields = ()
    list_filter = ('entidade', 'data', 'precisa_retorno')
    list_display = ('consulente', 'entidade', 'data')

    fieldsets = (
        (None, {
            'fields': (
                'consulente',
                'entidade',
                'data',
                'trabalhadores',
                'terapias_recomendadas',
                'precisa_retorno',
                'recomendacoes',
                'observacoes',
            )
        }),
    )




