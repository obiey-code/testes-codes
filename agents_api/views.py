# agents_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Agent
from .serializers import AgentSerializer

# --- Classe de Pagination ---
class AgentListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class AgentListAPIView(generics.ListAPIView):
    """
    API: /api/agents/list
    Liste paginée des agents.
    """
    
    # Optimisation : utiliser select_related('user') pour charger les données utilisateur en une seule requête
    queryset = Agent.objects.filter(is_active=True).select_related('user').order_by('user__last_name')
    
    # Serializer
    serializer_class = AgentSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = AgentListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par code agent, email, nom et prénom
    search_fields = ['agent_code', 'user__email', 'user__first_name', 'user__last_name']
    
    # Tri possible
    ordering_fields = ['agent_code', 'user__last_name', 'hire_date']
    ordering = ['user__last_name']