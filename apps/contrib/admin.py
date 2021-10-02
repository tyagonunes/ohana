from django.contrib import admin
from django.db import models
from .models import Consulente, Entidade, Entidade_tipo, Trabalhador

@admin.register(Consulente)
class ConsulenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'telefone')

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'data_nascimento',
                'endereco',
                'telefone'
            )
        }),
    )

@admin.register(Trabalhador)
class TrabalhadorAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'telefone')

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'data_nascimento',
                'endereco',
                'telefone'
            )
        }),
    )

@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ('tipo',)
    list_display = ('nome', 'tipo', 'descricao',)

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'tipo',
                'descricao',
            )
        }),
    )

@admin.register(Entidade_tipo)
class TipoEntidadeAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )