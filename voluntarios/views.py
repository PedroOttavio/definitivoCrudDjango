from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Voluntario
from .forms import VoluntarioModelForm

class VoluntariosView(LoginRequiredMixin, ListView):
    permission_required = 'voluntarios.view_voluntario'
    permission_denied_message = 'Acesso negado'
    model = Voluntario
    template_name = 'voluntarios.html'
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VoluntariosView, self).get_queryset()
        if buscar:
            return qs.filter(nome__icontains=buscar)
        
        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Nenhum voluntário encontrado.')
        

class VoluntarioAddView(LoginRequiredMixin, SuccessMessageMixin ,CreateView):
    permission_required = 'voluntarios.add_voluntario'
    permission_denied_message = 'Acesso negado'
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário cadastrado com sucesso.'
    
    
class VoluntarioUpdateView(SuccessMessageMixin, UpdateView):
    permission_required = 'voluntarios.update_voluntario'
    permission_denied_message = 'Acesso negado'
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário atualizado com sucesso.'
    
    
class VoluntarioDeleteView(SuccessMessageMixin, DeleteView):
    permission_required = 'voluntarios.delete_abrigo'
    permission_denied_message = 'Acesso negado'
    model = Voluntario
    template_name = 'voluntario_apagar.html'
    success_url = reverse_lazy('voluntarios')
    success_message = 'Voluntário apagado com sucesso.'
    
    