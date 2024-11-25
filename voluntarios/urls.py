from django.urls import path

from .views import VoluntariosView, VoluntarioAddView

urlpatterns = [
    path('voluntarios', VoluntariosView.as_view(), name='voluntarios'),
    path('voluntario/adicionar', VoluntarioAddView.as_view(), name='voluntario_adicionar'),
]


