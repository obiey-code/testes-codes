# repartitions_api/urls.py
from django.urls import path
from .views import RepartitionListAPIView

# Le préfixe de cet app sera '/api/repartitions/'
urlpatterns = [
    # URL: /api/repartitions/list
    path('list', RepartitionListAPIView.as_view(), name='repartition-list'),
]