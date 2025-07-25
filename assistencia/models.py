from django.db import models
from voluntarios.models import Voluntario
from vitimas.models import Vitima
from abrigos.models import Abrigo

# Create your models here.

class Assistencia(models.Model):
    
    STATUS_OPCOES = (
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Cancelado'),
    )
    
    PRIORIDADE_OPCOES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),

    )
    
    data = models.DateField();
    descricao = models.TextField(max_length=100)
    prioridade = models.CharField('Prioridade', max_length=20, help_text='Prioridade do serviço', choices=PRIORIDADE_OPCOES, default='B')
    voluntario = models.ForeignKey('voluntarios.Voluntario', related_name='voluntario', help_text='Voluntário que realizou o serviço', on_delete=models.CASCADE)
    vitima = models.ForeignKey('vitimas.Vitima', related_name='vitima', help_text='Vítima atendida', on_delete=models.CASCADE) 
    status = models.CharField('Status', max_length=20, help_text='Status do serviço', choices=STATUS_OPCOES, default='A')
    
    class Meta:
        verbose_name = 'Assistencia'
        verbose_name_plural = 'Assistencias'
        ordering = ['data'] #ordenar pela data, supostamente
 
        def __str__(self):
            return f'{self.descricao} - {self.voluntario} - {self.vitima}'
        
    
    # não precisa explicitar o abrigo
    
    
