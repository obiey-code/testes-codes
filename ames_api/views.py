# ames_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import AME
from .serializers import AMESerializer

# --- Classe de Pagination ---
class AMEListPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'size'
    max_page_size = 50

# --- Vue pour l'API de Liste ---
class AMEListAPIView(generics.ListAPIView):
    """
    API: /api/ames/list
    Liste paginée des entités AME.
    """
    
    # Récupérer la requête de base
    queryset = AME.objects.filter(is_active=True).order_by('name')
    
    # Serializer
    serializer_class = AMESerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = AMEListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par code et par nom
    search_fields = ['code', 'name', 'contact_person']
    
    # Tri possible
    ordering_fields = ['id', 'code', 'name']
    ordering = ['name']