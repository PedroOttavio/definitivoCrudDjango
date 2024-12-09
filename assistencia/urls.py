from django.urls import path
from .views import AssistenciasView, AssistenciaAddView, AssistenciaUpdateView, AssistenciaDeleteView



urlpatterns = [
    path('assistencias', AssistenciasView.as_view(), name='assistencias'),
    path('assistencia/adicionar', AssistenciaAddView.as_view(), name='assistencia_adicionar'),
    path('<int:pk>/assistencia/editar', AssistenciaUpdateView.as_view(), name='assistencia_editar'),
    path('<int:pk>/assistencia/apagar', AssistenciaDeleteView.as_view(), name='assistencia_apagar'),
]
