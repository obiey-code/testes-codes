# recettes_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Recette
from .serializers import RecetteSerializer

# --- Classe de Pagination ---
class RecetteListPagination(PageNumberPagination):
    page_size = 50 
    page_size_query_param = 'size'
    max_page_size = 200 # Souvent beaucoup d'enregistrements dans les recettes

# --- Vue pour l'API de Liste ---
class RecetteListAPIView(generics.ListAPIView):
    """
    API: /api/recettes/list
    Liste paginée des enregistrements de recettes.
    """
    
    # Optimisation : Charger toutes les entités liées (Caissier, Cabine, Site)
    queryset = Recette.objects.all().select_related('caissier', 'cabine', 'site').order_by('-timestamp')
    
    # Serializer
    serializer_class = RecetteSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = RecetteListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Caissier, Cabine, Site, Méthode ou Date/Montant
    filterset_fields = {
        'caissier': ['exact'],
        'cabine': ['exact'],
        'site': ['exact'],
        'payment_method': ['exact'],
        'timestamp': ['exact', 'gte', 'lte', 'date'], 
        'montant': ['gte', 'lte'], 
    }
    
    # Recherche textuelle (par référence de transaction, matricule caissier, nom de site/cabine)
    search_fields = ['transaction_ref', 'caissier__matricule_caissier', 'site__name', 'cabine__cabine_number']
    
    # Tri possible
    ordering_fields = ['timestamp', 'montant', 'payment_method']
    ordering = ['-timestamp']