# cabines_api/urls.py
from django.urls import path
from .views import CabineListAPIView

# Le préfixe de cet app sera '/api/cabines/'
urlpatterns = [
    # URL: /api/cabines/list
    path('list', CabineListAPIView.as_view(), name='cabine-list'),
]