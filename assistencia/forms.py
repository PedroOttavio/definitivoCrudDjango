from django import forms
from .models import Assistencia, Abrigo
from vitimas.models import Vitima
from voluntarios.models import Voluntario

class AssistenciaListForm(forms.ModelForm):
    vitima = forms.ModelChoiceField(label='Vítima', queryset=Vitima.objects.all(), required=False)
    voluntario = forms.ModelChoiceField(label='Voluntário', queryset=Voluntario.objects.all(), required=False)
    abrigo = forms.ModelChoiceField(label='Abrigo', queryset=Abrigo.objects.all(), required=False)

    class Meta:
        model = Assistencia
        fields = ['vitima', 'voluntario', 'abrigo']

class AssistenciaModelForm(forms.ModelForm):
    class Meta:
        model = Assistencia
        fields = ['data', 'descricao', 'prioridade', 'voluntario', 'vitima', 'status']
        
        error_messages = {
            'data': {
                'required': 'Data é obrigatória',
            },
            'descricao': {
                'required': 'Descrição é obrigatória',
            },
            'prioridade': {
                'required': 'Prioridade é obrigatória',
            },
            'voluntario': {
                'required': 'Voluntário é obrigatório',
            },
            'vitima': {
                'required': 'Vítima é obrigatória',
            },
            'status': {
                'required': 'Status é obrigatório',
            },
        }