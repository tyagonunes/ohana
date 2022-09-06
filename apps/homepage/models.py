from django.db import models
from .choices import STATUS_NOTICIA_CHOICES, STATUS_NOTICIA_CRIADA
from apps.base.mixins import BaseModel

class Noticia(BaseModel):
    titulo = models.CharField('Titulo', max_length=255)
    texto = models.TextField('Texto'),
    status = models.IntegerField('status', choices=STATUS_NOTICIA_CHOICES, default=STATUS_NOTICIA_CRIADA)
    url = models.SlugField(max_length=100)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

class Categoria(BaseModel):
    titulo = models.CharField('Titulo', max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
