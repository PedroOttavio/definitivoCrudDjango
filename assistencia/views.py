from django.shortcuts import render
from django.views.generic.list import ListView  
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin  # import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Assistencia
from .forms import AssistenciaListForm, AssistenciaModelForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView


# Create your views here.


class AssistenciasView(ListView):
    model = Assistencia
    template_name = 'assistencias.html'
    
    def get_context_data(self, **kwargs):
        context = super(AssistenciasView, self).get_context_data(**kwargs)
        if self.request.GET:
            form = AssistenciaListForm(self.request.GET)
        else:
            form = AssistenciaListForm()
        context['form'] = form
        return context
    
    
    def get_queryset(self):
        qs = super(AssistenciasView, self).get_queryset()
        if self.request.GET:
            form = AssistenciaListForm(self.request.GET)
            if form.is_valid():
                vitima = form.cleaned_data.get('vitima')
                voluntario = form.cleaned_data.get('voluntario')
                if vitima:
                    qs = qs.filter(vitima=vitima)
                if voluntario:
                    qs = qs.filter(voluntario=voluntario)
        
        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Nenhum registro de assistencia encontrado')
             
            
    class AssistenciaAddView(SuccessMessageMixin, CreateView):
        model = Assistencia
        form_class = AssistenciaModelForm
        template_name = "assistencia_form.html"
        success_url = reverse_lazy('assistencias')
        success_message = "Registro de assistência adicionado com sucesso"
    
    
    
    class AssistenciaUpdateView(SuccessMessageMixin, UpdateView):
        model = Assistencia
        form_class = AssistenciaModelForm
        template_name = "assistencia_form.html"
        success_url = reverse_lazy('assistencias')
        success_message = "Registro de assistência atualizado com sucesso"
        
    class AssistenciaDeleteView(SuccessMessageMixin, DeleteView):
        model = Assistencia
        template_name = "assistencia_apagar.html"
        success_url = reverse_lazy('assistencias')
        success_message = "Registro de assistência apagado com sucesso"