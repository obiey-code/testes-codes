# controles_api/urls.py
from django.urls import path
from .views import ControleListAPIView

# Le préfixe de cet app sera '/api/controles/'
urlpatterns = [
    # URL: /api/controles/list
    path('list', ControleListAPIView.as_view(), name='controle-list'),
]