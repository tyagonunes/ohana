from django.db import models


class Consulente(models.Model):
    cols = {
        'nome': 6,
        'cpf': 3,
        'data_nascimento': 3,
        'endereco': 6,
        'telefone': 3,
        'email': 3
    }
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField('Email', null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consulente'
        verbose_name_plural = 'Consulentes'


class Trabalhador(models.Model):
    cols = {
        'nome': 6,
        'cpf': 3,
        'data_nascimento': 3,
        'endereco': 6,
        'telefone': 3,
        'email': 3,
        'tipo_mediunidade': 6,
        'funcao': 6
    }
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField('Email', null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    tipo_mediunidade = models.ManyToManyField(
        'TipoMediunidade', 
        verbose_name='Tipos de mediunidade', 
        related_name='%(class)s_tipo_mediunidade',
        blank=True
    )
    funcao = models.ManyToManyField(
        'TrabalhadorFuncao',
        verbose_name='Funções',
        related_name='%(class)s_funcao',
        blank=True
    )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Trabalhador'
        verbose_name_plural = 'Trabalhadores'


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
                null=True, blank=True)
  
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


class TipoMediunidade(models.Model):
    cols = {
        'titulo': 6,
        'descricao': 12
    }
    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Tipo de mediunidade'
        verbose_name_plural = 'Tipos de mediunidade'

class TrabalhadorFuncao(models.Model):
    cols = {
        'titulo': 6,
        'descricao': 12
    }
    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Função do trabalhador'
        verbose_name_plural = 'Funções dos trabalhadores'
