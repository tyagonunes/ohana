from django.contrib import admin
from .models import Consulente, Entidade, TipoEntidade, TipoMediunidade, Trabalhador, TrabalhadorFuncao, Cidade, Estado, Terapia

@admin.register(Consulente)
class ConsulenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ('cidade', )
    list_display = ('nome', 'cpf', 'email', 'telefone')

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'cpf',
                'data_nascimento',
                'endereco',
                'cidade',
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

@admin.register(Terapia)
class TerapiaAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'descricao' )
    list_filter = ()
    list_display = ('titulo', 'descricao', )

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = ('nome', )
    list_filter = ('estado',)
    list_display = ('nome', 'estado', )

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    list_filter = ()
    list_display = ('nome', 'sigla', )