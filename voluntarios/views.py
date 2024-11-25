from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class VoluntarioAddView(CreateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    
    
class VoluntarioUpdateView(UpdateView):
    model = Voluntario
    form_class = VoluntarioModelForm
    template_name = 'voluntario_form.html'
    success_url = reverse_lazy('voluntarios')
    
    
class VoluntarioDeleteView(DeleteView):
    model = Voluntario
    template_name = 'voluntario_apagar.html'
    success_url = reverse_lazy('voluntarios')