# receveurs_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Receveur
from .serializers import ReceveurSerializer

# --- Classe de Pagination ---
class ReceveurListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class ReceveurListAPIView(generics.ListAPIView):
    """
    API: /api/receveurs/list
    Liste paginée des receveurs.
    """
    
    # Optimisation : Charger les données Agent et User en une seule requête (JOINTURE)
    queryset = Receveur.objects.filter(is_active=True).select_related('agent', 'agent__user').order_by('matricule_receveur')
    
    # Serializer
    serializer_class = ReceveurSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = ReceveurListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par matricule, code agent, email, nom ou prénom de l'utilisateur
    search_fields = [
        'matricule_receveur', 
        'agent__agent_code', 
        'agent__user__email', 
        'agent__user__last_name'
    ]
    
    # Tri possible
    ordering_fields = ['matricule_receveur', 'agent__user__last_name', 'is_supervisor']
    ordering = ['matricule_receveur']