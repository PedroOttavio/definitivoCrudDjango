from django.urls import path

from .views import VitimasView, VitimaAddView, VitimaUpdateView, VitimaDeleteView

urlpatterns = [
    path('vitimas', VitimasView.as_view(), name='vitimas'),
    path('vitima/adicionar/', VitimaAddView.as_view(), name='vitima_adicionar'),
    path('<int:pk>/vitima/editar/', VitimaUpdateView.as_view(), name='vitima_editar'),
    path('<int:pk>/vitima/apagar/', VitimaDeleteView.as_view(), name='vitima_apagar'),
]

