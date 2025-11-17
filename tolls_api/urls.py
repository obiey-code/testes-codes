# tolls_api/urls.py
from django.urls import path
from .views import TollSubscriberListAPIView

# Le préfixe de cet app sera '/api/toll-subscribers/'
urlpatterns = [
    # URL: /api/toll-subscribers/list
    path('list', TollSubscriberListAPIView.as_view(), name='toll-subscriber-list'),
]