# agents_api/urls.py
from django.urls import path
from .views import AgentListAPIView

# Le préfixe de cet app sera '/api/agents/'
urlpatterns = [
    # URL: /api/agents/list
    path('list', AgentListAPIView.as_view(), name='agent-list'),
]