from django.db import models
from django.contrib.auth.models import User
from .choices import CHOICE_SIM_NAO

class Trabalhador(models.Model):
    cols = {
        'nome': 4,
        'email': 4,
        'data_nascimento': 4,
        'cpf': 4,
        'endereco': 4,
        'cidade': 4,
        'telefone': 4,
        'ativo': 1,
    }
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
    data_ingresso = models.DateField('Data de ingresso no corpo mediunico', null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    cidade = models.ForeignKey(
                'cadastros_basicos.Cidade', 
                on_delete=models.PROTECT,
                related_name='%(class)s_cidade',
                null=True, blank=True
    )
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', null=True, blank=True)
   
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Trabalhador'
        verbose_name_plural = 'Trabalhadores'

class Consulente(models.Model):
    cols = {
        'nome': 6,
        'data_nascimento': 4,
        'email': 6,
        'telefone': 4,
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
    doencas_preexistentes = models.IntegerField('Tem doença(s) diagnosticada(s) por médico(s)?', choices=CHOICE_SIM_NAO, default=0)
    descricao_doencas_preexistentes = models.TextField('Quais?', blank=True, null=True)
    possui_marcapasso = models.IntegerField('É portador de marcapasso?', choices=CHOICE_SIM_NAO, default=0)
    toma_medicacao = models.IntegerField('Está tomando medicação?', choices=CHOICE_SIM_NAO, default=0)
    descricao_medicacao = models.TextField('Quais?', blank=True, null=True)
    motivo_atendimento = models.TextField('Motivo da procura pelo atendimento (o que procura obter?)', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consulente'
        verbose_name_plural = 'Consulentes'

