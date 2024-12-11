from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



from .models import Abrigo
from .forms import AbrigoModelForm, VoluntarioModelForm

class AbrigosView(LoginRequiredMixin, ListView):
    permission_required = 'abrigos.view_abrigo'
    permission_denied_message = 'Acesso negado: você não pode Visualizar Abrigos.'
    model = Abrigo
    template_name = 'abrigos.html'
    
    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(AbrigosView, self).get_queryset()
        
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
            
            
        if qs.count() > 0:
            paginator = Paginator(qs, 5)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem abrigos cadastrados.')
        

class AbrigoAddView(LoginRequiredMixin, SuccessMessageMixin ,CreateView):
    permission_required = 'abrigos.add_abrigo'
    permission_denied_message = 'Acesso negado.'
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos') 
    success_message = 'Abrigo cadastrado com sucesso.'
    
    
class AbrigoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'abrigos.update_abrigo'
    permission_denied_message = 'Acesso negado'
    model = Abrigo
    form_class = AbrigoModelForm
    template_name = 'abrigo_form.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Registro de abrigo alterado com sucesso.'
    
    
class AbrigoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'abrigos.delete_abrigo'
    permission_denied_message = 'Acesso negado'
    model = Abrigo
    template_name = 'abrigo_apagar.html'
    success_url = reverse_lazy('abrigos')
    success_message = 'Registro do abrigo apagado com sucesso.'
    


def Voluntarios_por_abrigo(request, pk):
    
    abrigo = Abrigo.objects.get(pk=pk)
    voluntarios = abrigo.voluntarios.all()
    return render(request, 'voluntarios_por_abrigo.html', {'abrigo': abrigo, 'voluntarios': voluntarios})


#adicionar vários voluntarios no combo box do abrigo, resta saber se vai funcionar

def adicionar_voluntarios(request, pk):
    abrigo = get_object_or_404(Abrigo, pk=pk)
    if request.method == 'POST':
        form = VoluntarioModelForm(request.POST)
        if form.is_valid():
            voluntarios_adicionar = form.cleaned_data.get('voluntarios', [])
            voluntarios_remover = form.cleaned_data.get('voluntarios_remover', [])
            abrigo.voluntarios.add(*voluntarios_adicionar)
            abrigo.voluntarios.remove(*voluntarios_remover)
            abrigo.save()
            messages.success(request, 'Voluntários atualizados com sucesso.')
            return redirect('abrigos')
    else:
        form = VoluntarioModelForm(initial={'voluntarios': abrigo.voluntarios.all()})
    return render(request, 'adicionar_voluntarios.html', {'form': form, 'abrigo': abrigo})