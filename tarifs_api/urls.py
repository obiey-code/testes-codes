# tarifs_api/urls.py
from django.urls import path
from .views import TarifListAPIView

# Le préfixe de cet app sera '/api/tarifs/'
urlpatterns = [
    # URL: /api/tarifs/list
    path('list', TarifListAPIView.as_view(), name='tarif-list'),
]