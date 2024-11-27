from django import forms

from .models import Vitima


class VitimaModelForm(forms.ModelForm):
    
    class Meta:
        model = Vitima
        fields = '__all__'
        
        error_messages = {
            'nome': {
                'required': 'O nome da vitima é um campo obrigatório.',
            },
            'fone': {
                'required': 'O telefone da vitima é um campo obrigatório.',
            },
            'data_resgate': {
                'required': 'A data de resgate da vitima é um campo obrigatório.',
            },
            'necessidades_especiais': {
                'required': 'As necessidades especiais da vitima é um campo obrigatório.',
            },
            'cpf': {
                'required': 'O CPF da vitima é um campo obrigatório.', 'unique': 'Este CPF já está cadastrado.',
            },
            'email': {
                'required': 'O e-mail da vitima é um campo obrigatório.', 'unique': 'Este e-mail já está cadastrado.',  
            },  
            'abrigos': {
                'required': 'O abrigo é um campo obrigatório.',
            },
            
        }