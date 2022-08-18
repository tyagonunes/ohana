from django.db import models

class Trabalhador(models.Model):
    cols = {
        'nome': 6,
        'cpf': 3,
        'data_nascimento': 3,
        'endereco': 9,
        'cidade': 3,
        'telefone': 5,
        'email': 6,
        'ativo': 1,
        'funcao': 6,
    }
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    data_nascimento = models.DateField('Data de nascimento')
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
   
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Trabalhador'
        verbose_name_plural = 'Trabalhadores'
