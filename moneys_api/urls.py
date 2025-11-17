# moneys_api/urls.py
from django.urls import path
from .views import MoneyListAPIView

# Le préfixe de cet app sera '/api/moneys/'
urlpatterns = [
    # URL: /api/moneys/list
    path('list', MoneyListAPIView.as_view(), name='money-list'),
]