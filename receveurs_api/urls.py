# receveurs_api/urls.py
from django.urls import path
from .views import ReceveurListAPIView

# Le préfixe de cet app sera '/api/receveurs/'
urlpatterns = [
    # URL: /api/receveurs/list
    path('list', ReceveurListAPIView.as_view(), name='receveur-list'),
]