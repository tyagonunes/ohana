from django.db import models
from apps.cadastros_basicos.models import Banho, Entidade, Terapia
from apps.usuario.models import Trabalhador, Consulente
from apps.base.mixins import BaseModel

from .choices import CHOICES_STATUS_ATENDIMENTO

class AtendimentoPretoVelho(BaseModel):
    cols = {
        'consulente': 3,
        'guia': 3,
        'medium': 3,
        'mediador': 3,
        'data': 3,
        'precisa_retorno': 3,
        'recomendacoes': 12,
        'status': 3
    }
    consulente = models.ForeignKey(
        Consulente,
        on_delete=models.PROTECT,
        verbose_name='Consulente',
        related_name='%(class)s_consulente',
        null=True, blank=True
    )
    mediador = models.ForeignKey(
        Trabalhador,
        on_delete=models.PROTECT,
        verbose_name='Mediador',
        related_name='%(class)s_mediador',
        null=True, blank=True
    )
    medium = models.ForeignKey(
        Trabalhador,
        on_delete=models.PROTECT,
        verbose_name='Médium',
        related_name='%(class)s_medium',
        null=True, blank=True
    )
    guia = models.ForeignKey(
        Entidade,
        on_delete=models.PROTECT,
        verbose_name='Guia',
        related_name='%(class)s_guia',
        null=True, blank=True
    )
    status = models.IntegerField('Status', choices=CHOICES_STATUS_ATENDIMENTO, blank=True, null=True)
    precisa_retorno = models.BooleanField('Precisa de retorno', default=False)
    data = models.DateField('Data')
    recomendacoes = models.TextField('Recomendações', null=True, blank=True)

    def get_banhos(self):
        return AtendimentoPretoVelhoBanho.objects.filter(atendimento_id=self.id)
    
    def get_terapias(self):
        return AtendimentoPretoVelhoTerapia.objects.filter(atendimento_id=self.id)

    def __str__(self):
        return '{} - {}'.format(self.consulente, self.data.strftime('%d/%m/%Y'))
    
    class Meta:
        verbose_name = 'Atendimento de Preto Velho'
        verbose_name_plural = 'Atendimentos de Pretos Velhos'
        ordering = ['-data']


class AtendimentoPretoVelhoTerapia(BaseModel):
    cols = {
        'terapia': 6,
        'data': 6,
        'instrucoes': 12
    }
    atendimento = models.ForeignKey(
        AtendimentoPretoVelho,
        on_delete=models.PROTECT,
        related_name='%(class)s_atendimento'
    )
    terapia = models.ForeignKey(
        Terapia,
        on_delete=models.PROTECT,
        verbose_name='Terapia',
        related_name='%(class)s_terapia',
    )
    data = models.DateField('Data', blank=True, null=True)
    instrucoes = models.TextField('Instruções', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.terapia)

    class Meta:
        verbose_name = 'Atendimento Terapia'
        verbose_name_plural = 'Atendimentos Terapias'

class AtendimentoPretoVelhoBanho(BaseModel):
    cols = {
        'banho': 6,
        'instrucoes': 12
    }
    atendimento = models.ForeignKey(
        AtendimentoPretoVelho,
        on_delete=models.PROTECT,
        related_name='%(class)s_atendimento'
    )
    banho = models.ForeignKey(
        Banho,
        on_delete=models.PROTECT,
        related_name='%(class)s_banho'
    )
    instrucoes = models.TextField('Instruções', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.atendimento, self.banho)
    class Meta:
        verbose_name = 'Atendimento Banho'
        verbose_name_plural = 'Atendimentos Banhos'