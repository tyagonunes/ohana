from django.contrib import admin
from .models import Entidade, TipoEntidade, TipoMediunidade, Cidade, Estado, Terapia, Faixa

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

@admin.register(Faixa)
class FaixaAdmin(admin.ModelAdmin):
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