from django.db import models


class Consulente(models.Model):
    cols = {
        'nome': 8,
        'data_nascimento': 4,
        'endereco': 8,
        'telefone': 4
    }
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consulente'
        verbose_name_plural = 'Consulentes'


class Trabalhador(models.Model):
    cols = {
        'nome': 8,
        'data_nascimento': 4,
        'endereco': 8,
        'telefone': 4
    }
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    endereco = models.CharField('Endereço', max_length=255, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    
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
    tipo = models.ForeignKey('Entidade_tipo',
                on_delete=models.PROTECT,
                related_name='%(class)s_entidade_tipo',
                null=True, blank=True)
  
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'



class Entidade_tipo(models.Model):
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
