# from django.db import models
# from voluntarios.models import Voluntario
# from vitimas.models import Vitima
# from abrigos.models import Abrigo

# # Create your models here.

# class Assistencia(models.model):
    
#     STATUS_OPCOES = (
#         ('A', 'Agendado'),
#         ('R', 'Realizado'),
#         ('C', 'Cancelado'),
#     )
    
#     PRIORIDADE_OPCOES = (
#         ('A', 'Alta'),
#         ('M', 'Média'),
#         ('B', 'Baixa'),
#     )
    
#     data = models.DateField();
#     descricao = models.TextField('Descrição', help_text='Descrição do serviço')
#     prioridade = models.CharField('Prioridade', max_length=20, help_text='Prioridade do serviço', choices=PRIORIDADE_OPCOES, default='B')
#     voluntario = models.ForeignKey('voluntarios.Voluntario', related_name='abrigos', help_text='Voluntário que realizou o serviço')
#     vitima = models.ForeignKey('vitimas.Vitima', related_name='abrigos', help_text='Vítima atendida') 
#     status = models.CharField('Status', max_length=20, help_text='Status do serviço', choices=STATUS_OPCOES, default='A')
    
#     class Meta:
#         verbose_name = 'Assistencia'
#         verbose_name_plural = 'Assistencias'
        
#         def __str__(self):
#             return f'{self.descricao} - {self.voluntario} - {self.vitima}'
        
    
#     # não precisa explicitar o abrigo
    
    
