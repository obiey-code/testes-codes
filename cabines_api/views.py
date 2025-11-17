# cabines_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Cabine
from .serializers import CabineSerializer

# --- Classe de Pagination ---
class CabineListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class CabineListAPIView(generics.ListAPIView):
    """
    API: /api/cabines/list
    Liste paginée des cabines de péage.
    """
    
    # Optimisation : utiliser select_related('site') pour charger les données du site en une seule requête
    queryset = Cabine.objects.filter(is_active=True).select_related('site').order_by('site__name', 'cabine_number')
    
    # Serializer
    serializer_class = CabineSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = CabineListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par numéro de cabine ou par nom de site lié
    search_fields = ['cabine_number', 'site__name']
    
    # Tri possible
    ordering_fields = ['cabine_number', 'site__name', 'direction']
    ordering = ['site__name', 'cabine_number']