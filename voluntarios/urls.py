from django.urls import path

from .views import VoluntariosView, VoluntarioAddView, VoluntarioUpdateView, VoluntarioDeleteView

urlpatterns = [
    path('voluntarios', VoluntariosView.as_view(), name='voluntarios'),
    path('voluntario/adicionar', VoluntarioAddView.as_view(), name='voluntario_adicionar'),
    path('<int:pk>/voluntario/editar', VoluntarioUpdateView.as_view(), name='voluntario_editar'),
    path('<int:pk>/voluntario/apagar', VoluntarioDeleteView.as_view(), name='voluntario_apagar'),
]


