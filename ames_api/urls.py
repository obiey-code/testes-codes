# ames_api/urls.py
from django.urls import path
from .views import AMEListAPIView

# Le préfixe de cet app sera '/api/ames/'
urlpatterns = [
    # URL: /api/ames/list
    path('list', AMEListAPIView.as_view(), name='ame-list'),
]