from django.contrib import admin
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from .models import Consulente, Entidade, TipoEntidade, TipoMediunidade, Trabalhador, TrabalhadorFuncao 

@admin.register(Consulente)
class ConsulenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ()
    list_display = ('nome', 'cpf', 'email', 'telefone')

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'cpf',
                'data_nascimento',
                'endereco',
                'email',
                'telefone'
            )
        }),
    )

@admin.register(Trabalhador)
class TrabalhadorAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'cpf' )
    list_filter = ('tipo_mediunidade', 'funcao')
    list_display = ('nome', 'cpf', 'email', 'telefone',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    
    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'cpf',
                'data_nascimento',
                'endereco',
                'telefone',
                'email',
                'tipo_mediunidade',
                'funcao'
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

@admin.register(TipoEntidade)
class TipoEntidadeAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )

@admin.register(TipoMediunidade)
class TipoMediunidadeAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )

@admin.register(TrabalhadorFuncao)
class TrabalhadorFuncaoAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )