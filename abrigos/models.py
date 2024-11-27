from django.db import models
from voluntarios.models import Voluntario  # Import Voluntario class



# Create your models here.


class Abrigo(models.Model):
    nome = models.CharField('Nome do abrigo', max_length=100, help_text='Nome do abrigo')
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço do abrigo')
    capacidade = models.IntegerField('Capacidade', help_text='Capacidade do abrigo')
    fone = models.CharField('Telefone', max_length=20, help_text='Telefone do abrigo')
    tipo = models.CharField('Tipo', max_length=20, help_text='Tipo do abrigo')
    descricao = models.CharField('Descrição', max_length=50, help_text='Descrição do abrigo')
    status = models.CharField('Status', max_length=20, help_text='Status do abrigo')
    voluntarios = models.ManyToManyField('voluntarios.Voluntario', related_name='abrigos', help_text='Voluntários trabalhando neste abrigo')
    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'

    def __str__(self):
        return self.nome