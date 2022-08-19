from django.db import models
from .choices import ESTADOS_CHOICES

class Entidade(models.Model):
    cols = {
        'nome': 8,
        'tipo': 4,
        'descricao': 12
    }
    nome = models.CharField('Nome', max_length=255)
    descricao = models.TextField('Descrição', null=True, blank=True)
    tipo = models.ForeignKey('TipoEntidade',
                on_delete=models.PROTECT,
                related_name='%(class)s_tipo',
                null=True, blank=True
    )
  
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'


class TipoEntidade(models.Model):
    cols = {
        'titulo': 6,
        'descricao': 12
    }
    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Tipo de entidade'
        verbose_name_plural = 'Tipos de entidades'

class Terapia(models.Model):
    cols = {
        'titulo': 6,
        'descricao': 12
    }
    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição', null=True, blank=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'

class Cidade(models.Model):
    nome = models.CharField('Nome', max_length=255)
    estado = models.IntegerField(
        'Estado',
        choices=ESTADOS_CHOICES,
        null=True, blank=True
    )
    
    def __str__(self):
        return '{} - {}'.format(self.nome, self.get_estado_display())
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'