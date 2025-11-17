# caissiers_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Caissier
from .serializers import CaissierSerializer

# --- Classe de Pagination ---
class CaissierListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class CaissierListAPIView(generics.ListAPIView):
    """
    API: /api/caissiers/list
    Liste paginée des caissiers.
    """
    
    # Optimisation : Charger les données Agent et User en une seule requête (JOINTURE)
    queryset = Caissier.objects.filter(is_active=True).select_related('agent', 'agent__user').order_by('matricule_caissier')
    
    # Serializer
    serializer_class = CaissierSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = CaissierListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par matricule, code agent, email, nom ou prénom de l'utilisateur
    search_fields = [
        'matricule_caissier', 
        'agent__agent_code', 
        'agent__user__email', 
        'agent__user__last_name'
    ]
    
    # Tri possible
    ordering_fields = ['matricule_caissier', 'agent__user__last_name']
    ordering = ['matricule_caissier']