# equipements_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Equipement
from .serializers import EquipementSerializer

# --- Classe de Pagination ---
class EquipementListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class EquipementListAPIView(generics.ListAPIView):
    """
    API: /api/equipements/list
    Liste paginée des équipements.
    """
    
    # Optimisation : Charger les données Cabine et Site en une seule requête
    queryset = Equipement.objects.filter(is_active=True).select_related('cabine', 'cabine__site').order_by('name')
    
    # Serializer
    serializer_class = EquipementSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = EquipementListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Cabine, ID de Site (via cabine__site) ou Statut exact
    filterset_fields = {
        'cabine': ['exact'],
        'cabine__site': ['exact'],
        'status': ['exact'],
    }
    
    # Recherche textuelle
    search_fields = ['name', 'serial_number', 'cabine__cabine_number', 'cabine__site__name']
    
    # Tri possible
    ordering_fields = ['serial_number', 'name', 'status', 'last_check']
    ordering = ['name']