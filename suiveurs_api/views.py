# suiveurs_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Suiveur
from .serializers import SuiveurSerializer

# --- Classe de Pagination ---
class SuiveurListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class SuiveurListAPIView(generics.ListAPIView):
    """
    API: /api/suiveurs/list
    Liste paginée des suiveurs.
    """
    
    # Optimisation : Charger les données Agent et User en une seule requête (JOINTURE)
    queryset = Suiveur.objects.filter(is_active=True).select_related('agent', 'agent__user').order_by('matricule_suiveur')
    
    # Serializer
    serializer_class = SuiveurSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = SuiveurListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par matricule, code agent, email, nom ou prénom de l'utilisateur
    search_fields = [
        'matricule_suiveur', 
        'agent__agent_code', 
        'agent__user__email', 
        'agent__user__last_name'
    ]
    
    # Tri possible
    ordering_fields = ['matricule_suiveur', 'agent__user__last_name', 'is_field_agent']
    ordering = ['matricule_suiveur']