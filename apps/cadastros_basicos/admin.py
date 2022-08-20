from django.contrib import admin
from .models import Entidade, TipoEntidade, Cidade, Terapia, Ingrediente

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

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    search_fields = ('titulo', )
    list_display = ('titulo', 'descricao', )
