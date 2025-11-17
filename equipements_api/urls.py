# equipements_api/urls.py
from django.urls import path
from .views import EquipementListAPIView

# Le préfixe de cet app sera '/api/equipements/'
urlpatterns = [
    # URL: /api/equipements/list
    path('list', EquipementListAPIView.as_view(), name='equipement-list'),
]