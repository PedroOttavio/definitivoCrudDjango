from django import forms

from .models import Abrigo, Voluntario

class AbrigoModelForm(forms.ModelForm):
    
    class Meta:
        model = Abrigo
        fields = '__all__'
        
        error_messages = {
            'nome': {
                'required': "O nome do abrigo é obrigatório",
            },
            'endereco': {
                'required': "O endereço do abrigo é obrigatório",
            },  
            'capacidade': {
                'required': "A capacidade do abrigo é obrigatório",
            },
            'fone': {
                'required': "O telefone do abrigo é obrigatório",
            },
            'tipo': {
                'required': "O tipo do abrigo é obrigatório",
            },
            'descricao': {
                'required': "A descrição do abrigo é obrigatório",
            },
            'status': {
                'required': "O status do abrigo é obrigatório",
            },
        }
        
        
        # classe voluntario, para podermos adicionar vários voluntarios na interface do abrigo
class VoluntarioModelForm(forms.Form):
    
    voluntarios = forms.ModelMultipleChoiceField(
        queryset=Voluntario.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Adicionar Voluntários"
        
    )
    voluntarios_remover = forms.ModelMultipleChoiceField(
        queryset=Voluntario.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Remover Voluntários"
    )