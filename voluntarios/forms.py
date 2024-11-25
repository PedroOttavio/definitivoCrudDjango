from django import forms

from .models import Voluntario

class VoluntarioModelForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'
        
        error_messages = {
            'nome': {
                'required': 'O nome do voluntário é um campo obrigatório.',
            },
            'especialidade': {
                'required': 'A especialidade do voluntário é um campo obrigatório.',
            },
            'disponibilidade': {
                'required': 'A disponibilidade do voluntário é um campo obrigatório.',
            },
            'experiencia': {
                'required': 'A experiência do voluntário é um campo obrigatório.',
            },
            
            'cpf': {
                'required': 'O CPF do voluntário é um campo obrigatório.', 'unique': 'Este CPF já está cadastrado.',
            },
            'fone': {
                'required': 'O telefone do voluntário é um campo obrigatório.',
            },
            
        }