# manquants_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Manquant
from .serializers import ManquantSerializer

# --- Classe de Pagination ---
class ManquantListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class ManquantListAPIView(generics.ListAPIView):
    """
    API: /api/manquants/list
    Liste paginée des manquants (déficits).
    """
    
    # Optimisation : Charger les données Caissier, Agent et User
    queryset = Manquant.objects.all().select_related(
        'caissier', 
        'caissier__agent', 
        'caissier__agent__user'
    ).order_by('-date_manquant')
    
    # Serializer
    serializer_class = ManquantSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = ManquantListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Caissier, statut résolu ou date
    filterset_fields = {
        'caissier': ['exact'],
        'is_resolved': ['exact'],
        'date_manquant': ['exact', 'gte', 'lte'], # Filtrage par date/période
        'montant': ['gte', 'lte'], # Filtrage par montant min/max
    }
    
    # Recherche textuelle (par justification, matricule caissier)
    search_fields = ['justification', 'caissier__matricule_caissier', 'caissier__agent__user__last_name']
    
    # Tri possible
    ordering_fields = ['date_manquant', 'montant', 'is_resolved']
    ordering = ['-date_manquant']