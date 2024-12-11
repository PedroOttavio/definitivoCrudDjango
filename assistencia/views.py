from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Assistencia
from django.core.mail import send_mail
from .forms import AssistenciaListForm, AssistenciaModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

class AssistenciasView(LoginRequiredMixin, ListView):
    permission_required = 'assistencia.view_assistencia'
    permission_denied_message = 'Acesso negado'
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
            messages.info(self.request, 'Nenhum registro de assistência encontrado')
            return qs

class AssistenciaAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'assistencia.add_assistencia'
    permission_denied_message = 'Acesso negado'
    model = Assistencia
    form_class = AssistenciaModelForm
    template_name = "assistencia_form.html"
    success_url = reverse_lazy('assistencias')
    success_message = "Registro de assistência adicionado com sucesso"
    
        
    def form_valid(self, form):
        response = super().form_valid(form)
        if form.instance.status in ['Realizado', 'R']:
            self.enviar_email(form.instance)
        return response
    
    def enviar_email(self, assistencia):
        email = []
        email.append(assistencia.vitima.email)
        descricao = []

        dados = {'vitima': assistencia.vitima.nome, 'voluntario': assistencia.voluntario.nome, 
                 'data': assistencia.data, 'hora': assistencia.hora,
                 'descricao': assistencia.descricao}
        
        texto_email = render_to_string('emails/texto_email.txt', dados)
        html_email = render_to_string('emails/texto_email.html', dados)
        send_mail(
                  subject='Assistencia prestada', 
                  message=texto_email,
                  from_email='pedroottavioss@gmail.com',
                  recipient_list=email,
                  html_message=html_email, 
                  fail_silently=False
        )
        return redirect('assistencias')
    


class AssistenciaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'assistencia.update_assistencia'
    permission_denied_message = 'Acesso negado'
    model = Assistencia
    form_class = AssistenciaModelForm
    template_name = "assistencia_form.html"
    success_url = reverse_lazy('assistencias')
    success_message = "Registro de assistência atualizado com sucesso"

class AssistenciaDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'assistencia.delete_assistencia'
    permission_denied_message = 'Acesso negado'
    model = Assistencia
    template_name = "assistencia_apagar.html"
    success_url = reverse_lazy('assistencias')
    success_message = "Registro de assistência apagado com sucesso"
    
    
    