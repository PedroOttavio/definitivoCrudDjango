from django.db import models
from django.db.models.functions import Upper
from stdimage import StdImageField
from voluntarios.models import Pessoa


# Create your models here.

class Vitima(Pessoa):
    data_resgate = models.DateField('Data do resgate', help_text='Data do resgate da vítima')
    status = models.CharField('Status', max_length=20, help_text='Status da vítima')
    # abrigo = models.ForeignKey('Abrigo', on_delete=models.PROTECT, verbose_name='Abrigo', help_text='Abrigo da vítima')
    familiares_localizados = models.BooleanField('Familiares localizados', help_text='Familiares localizados')
    numero_dependentes = models.IntegerField('Número de dependentes', help_text='Número de dependentes da vítima')
    necessidades_especiais = models.CharField('Necessidades especiais', max_length=50, help_text='Necessidades especiais da vítima')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    foto = StdImageField('Foto', upload_to='vitimas', delete_orphans=True, null = True, blank= True)
    # responsavel_cadastro = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='Responsável pelo cadastro', help_text='Responsável pelo cadastro da vítima')
    
    
    class Meta:
        verbose_name = 'Vítima'
        verbose_name_plural = 'Vítimas'
        
        
    def __str__(self):
        return super().nome