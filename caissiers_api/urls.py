# caissiers_api/urls.py
from django.urls import path
from .views import CaissierListAPIView

# Le préfixe de cet app sera '/api/caissiers/'
urlpatterns = [
    # URL: /api/caissiers/list
    path('list', CaissierListAPIView.as_view(), name='caissier-list'),
]