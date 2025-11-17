# controles_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend # Pour le filtrage précis
from .models import Controle
from .serializers import ControleSerializer

# --- Classe de Pagination ---
class ControleListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class ControleListAPIView(generics.ListAPIView):
    """
    API: /api/controles/list
    Liste paginée des contrôles effectués.
    """
    
    # Optimisation : Charger les données Site, Agent, et User de l'Agent
    queryset = Controle.objects.all().select_related('site', 'agent', 'agent__user').order_by('-control_date')
    
    # Serializer
    serializer_class = ControleSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = ControleListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Site, ID d'Agent ou Résultat exact
    filterset_fields = {
        'site': ['exact'],
        'agent': ['exact'],
        'result': ['exact'],
        'control_date': ['gte', 'lte', 'date'], # Filtrage par date/période
    }
    
    # Recherche textuelle
    search_fields = ['notes', 'agent__agent_code', 'site__name']
    
    # Tri possible
    ordering_fields = ['control_date', 'site__name', 'agent__agent_code', 'result']
    ordering = ['-control_date']