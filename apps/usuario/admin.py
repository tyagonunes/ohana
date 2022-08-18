from django.contrib import admin
from .models import Trabalhador


@admin.register(Trabalhador)
class TrabalhadorAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf' )
    list_filter = ()
    list_display = ('nome', 'cpf', 'email', 'telefone',)
    
    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'cpf',
                'data_nascimento',
                'endereco',
                'cidade',
                'email',
                'telefone',
                'ativo',
            )
        }),
    )
