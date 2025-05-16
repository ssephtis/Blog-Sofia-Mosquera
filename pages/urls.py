from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    about_view,
    CreatePageView,
    UpdatePageView,
    DeletePageView
)

urlpatterns = [
    # Home: listado de entradas
    path('', PageListView.as_view(), name='pages_list'),

    # Página estática "Acerca de mí"
    path('about/', about_view, name='about'),

    # Crear nueva entrada
    path('create/', CreatePageView.as_view(), name='page_create'),

    # Ver detalle de una entrada
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),

    # Editar una entrada existente
    path('<int:pk>/edit/', UpdatePageView.as_view(), name='page_edit'),

    # Borrar una entrada existente
    path('<int:pk>/delete/', DeletePageView.as_view(), name='page_delete'),
]
