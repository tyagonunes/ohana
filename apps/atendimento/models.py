from django.db import models
from .choices import CHOICE_ALTER
from django.contrib.auth.models import User
from apps.cadastros_basicos.models import Entidade
from apps.usuario.models import Trabalhador

class Atendimento(models.Model):
    cols = {
        'consulente': 3,
        'guia': 3,
        'medium': 3,
        'mediador': 3,
        'data': 3,
        'precisa_retorno': 3,
        'recomendacoes': 12,
    }
    consulente = models.ForeignKey(
        'Consulente',
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
    precisa_retorno = models.BooleanField('Precisa de retorno', default=False)
    data = models.DateField('Data')
    recomendacoes = models.TextField('Recomendações', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.consulente, self.data.strftime('%d/%m/%Y'))
    
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['-data']


class Consulente(models.Model):
    cols = {
        'nome': 6,
        'data_nascimento': 6,
        'email': 3,
        'telefone': 3,
        'telefone_whatsapp': 4,
        'possui_marcapasso': 12,
        'doencas_preexistentes': 12,
        'descricao_doencas_preexistentes': 12,
        'descricao_medicacao': 12,
        'motivo_atendimento': 12

    }
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField('Email', unique=True, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    telefone_whatsapp = models.BooleanField('Telefone é Whatsapp', default=False)
    doencas_preexistentes = models.IntegerField('Tem doença(s) diagnosticada(s) por médico(s)?', choices=CHOICE_ALTER, default=0)
    descricao_doencas_preexistentes = models.TextField('Quais?', blank=True, null=True)
    possui_marcapasso = models.IntegerField('É portador de marcapasso?', choices=CHOICE_ALTER, default=0)
    toma_medicacao = models.IntegerField('Está tomando medicação?', choices=CHOICE_ALTER, default=0)
    descricao_medicacao = models.TextField('Quais?', blank=True, null=True)
    motivo_atendimento = models.TextField('Motivo da procura pelo atendimento (o que procura obter?)', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consulente'
        verbose_name_plural = 'Consulentes'