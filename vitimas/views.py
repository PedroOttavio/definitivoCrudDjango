
# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages


from .models import Vitima
from .forms import VitimaModelForm

class VitimasView(ListView):
    model = Vitima
    template_name = 'vitimas.html'
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VitimasView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        
        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Nenhum registro de vitima encontrado.')
        

class VitimaAddView(SuccessMessageMixin ,CreateView):
    model = Vitima
    form_class = VitimaModelForm
    template_name = 'vitima_form.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Vitima cadastrada com sucesso.'
    
    
class VitimaUpdateView(SuccessMessageMixin, UpdateView):
    model = Vitima
    form_class = VitimaModelForm
    template_name = 'vitima_form.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Registro de vitima atualizado com sucesso.'
    
    
class VitimaDeleteView(SuccessMessageMixin, DeleteView):
    model = Vitima
    template_name = 'vitima_apagar.html'
    success_url = reverse_lazy('vitimas')
    success_message = 'Registro de vitima apagado com sucesso.'
    
    