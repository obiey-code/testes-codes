# tarifs_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Tarif
from .serializers import TarifSerializer

# --- Classe de Pagination ---
class TarifListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class TarifListAPIView(generics.ListAPIView):
    """
    API: /api/tarifs/list
    Liste paginée des tarifs.
    """
    
    # Optimisation : Charger les données Site
    queryset = Tarif.objects.all().select_related('site').order_by('site__name', 'vehicle_type')
    
    # Serializer
    serializer_class = TarifSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Site, Type de Véhicule, Statut, Montant ou Date
    filterset_fields = {
        'site': ['exact'],
        'vehicle_type': ['exact'],
        'is_active': ['exact'],
        'montant': ['gte', 'lte'], 
        'start_date': ['exact', 'gte', 'lte'],
    }
    
    # Recherche textuelle (par nom de site)
    search_fields = ['site__name', 'vehicle_type']
    
    # Tri possible
    ordering_fields = ['montant', 'start_date', 'site__name', 'vehicle_type']
    ordering = ['site__name', 'vehicle_type']