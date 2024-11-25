from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome completo')
    idade = models.IntegerField('Idade', help_text='Idade da pessoa')
    fone = models.CharField('Telefone', max_length=15, help_text='Telefone de contato')
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço da pessoa')
    email = models.EmailField('E-mail', max_length=100, help_text='E-mail da pessoa')
    cpf = models.CharField('CPF', max_length=14, help_text='CPF da pessoa', unique=True)
    sexo = models.CharField('Sexo', max_length=1, help_text='Sexo da pessoa')
    
    class Meta:
        abstract = True
        
    
class Voluntario(Pessoa):
    especialidade = models.CharField('Especialidade', max_length=100, help_text='Especialidade do voluntário')
    disponibilidade = models.CharField('Disponibilidade', max_length=100, help_text='Horários disponíveis')
    experiencia = models.CharField('Experiência', max_length=100, help_text='Experiência anterior')
    
    
    class Meta:
        verbose_name = 'Voluntário'
        verbose_name_plural = 'Voluntários'
        
        def __str__(self):
            return self.nome
    
    
    