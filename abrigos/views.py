from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages



from .models import Abrigo
from .forms import AbrigoModelForm

class AbrigosView(ListView):
    model = Abrigo
    template_name = 'abrigos.html'
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AbrigosView, self).get_queryset()
        
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
            
            
        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem abrigos cadastrados.')
        

class AbrigoAddView(SuccessMessageMixin ,CreateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos') 
    success_message = 'Abrigo cadastrado com sucesso.'
    
    
class AbrigoUpdateView(SuccessMessageMixin, UpdateView):
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Registro de abrigo alterado com sucesso.'
    
    
class AbrigoDeleteView(SuccessMessageMixin, DeleteView):
    model = Abrigo
    template_name = 'abrigo_apagar.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Registro do abrigo apagado com sucesso.'
    
    