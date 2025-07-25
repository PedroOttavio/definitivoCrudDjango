from django.urls import path
from .views import AbrigosView, AbrigoAddView, AbrigoUpdateView, AbrigoDeleteView, Voluntarios_por_abrigo, adicionar_voluntarios

urlpatterns = [
    path('abrigos', AbrigosView.as_view(), name='abrigos'),
    path('abrigo/adicionar/', AbrigoAddView.as_view(), name='abrigo_adicionar'),
    path('<int:pk>/abrigo/editar/', AbrigoUpdateView.as_view(), name='abrigo_editar'),
    path('<int:pk>/abrigo/apagar/', AbrigoDeleteView.as_view(), name='abrigo_apagar'),
    path('<int:pk>/abrigo/', Voluntarios_por_abrigo, name='abrigo_voluntarios'),
    path('<int:pk>/abrigo/adicionar_voluntarios/', adicionar_voluntarios, name='adicionar_voluntarios'),
]