# recettes_api/urls.py
from django.urls import path
from .views import RecetteListAPIView

# Le préfixe de cet app sera '/api/recettes/'
urlpatterns = [
    # URL: /api/recettes/list
    path('list', RecetteListAPIView.as_view(), name='recette-list'),
]