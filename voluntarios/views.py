from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Voluntario
from .forms import VoluntarioModelForm

class VoluntariosView(ListView):
    model = Voluntario
    template_name = 'voluntarios.html'
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VoluntariosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        return qs
    
        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Nenhum voluntário encontrado.')
        

class VoluntarioAddView(SuccessMessageMixin ,CreateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário cadastrado com sucesso.'
    
    
class VoluntarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário atualizado com sucesso.'
    
    
class VoluntarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Voluntario
    template_name = 'voluntario_apagar.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário apagado com sucesso.'
    
    