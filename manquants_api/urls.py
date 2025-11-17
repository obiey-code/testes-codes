# manquants_api/urls.py
from django.urls import path
from .views import ManquantListAPIView

# Le préfixe de cet app sera '/api/manquants/'
urlpatterns = [
    # URL: /api/manquants/list
    path('list', ManquantListAPIView.as_view(), name='manquant-list'),
]