from django.db import models

class ConsultaPretosVelhos(models.Model):
    cols = {
        'consulente': 4,
        'entidade': 4,
        'trabalhadores': 6,
        'data': 4,
        'precisa_retorno': 4,
        'terapias_recomendadas': 4,
        'recomendacoes': 12,
        'observacoes': 12
    }
    consulente = models.ForeignKey(
        'usuario.Consulente',
        on_delete=models.PROTECT,
        verbose_name='Consulente',
        related_name='%(class)s_consulente',
        null=True, blank=True
    )
    entidade = models.ForeignKey('cadastros_basicos.Entidade',
        on_delete=models.PROTECT,
        verbose_name='Entidade',
        related_name='%(class)s_entidade',
        null=True, blank=True
    )
    trabalhadores = models.ManyToManyField(
        'usuario.Trabalhador', 
        verbose_name='Trabalhadores', 
        related_name='%(class)s_trabalhadores'
    )
    precisa_retorno = models.BooleanField('Precisa de retorno', default=False)
    terapias_recomendadas = models.ManyToManyField(
        'cadastros_basicos.Terapia', 
        verbose_name='Terapias recomendadas', 
        related_name='%(class)s_terapias'
    )
    data = models.DateField('Data')
    recomendacoes = models.TextField('Recomendações', null=True, blank=True)
    observacoes = models.TextField('Observações', null=True, blank=True)


    def __str__(self):
        return '{} - {}'.format(self.consulente, self.data)
    
    class Meta:
        verbose_name = 'Consulta Preto Velho'
        verbose_name_plural = 'Consulta Pretos Velhos'


class AgendaLibertacao(models.Model):
    cols = {
        'data': 6,
        'consulentes': 12
    }
    data = models.DateField('Data')
    consulentes = models.ManyToManyField(
        'usuario.Consulente', 
        verbose_name='Consulentes', 
        related_name='%(class)s_consulentes'
    )

    def __str__(self):
        return str(self.data)
    class Meta:
        verbose_name = 'Agenda libertação'
        verbose_name_plural = 'Agenda libertação'
    