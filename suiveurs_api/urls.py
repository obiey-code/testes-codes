# suiveurs_api/urls.py
from django.urls import path
from .views import SuiveurListAPIView

# Le préfixe de cet app sera '/api/suiveurs/'
urlpatterns = [
    # URL: /api/suiveurs/list
    path('list', SuiveurListAPIView.as_view(), name='suiveur-list'),
]