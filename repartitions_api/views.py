# repartitions_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Repartition
from .serializers import RepartitionSerializer

# --- Classe de Pagination ---
class RepartitionListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class RepartitionListAPIView(generics.ListAPIView):
    """
    API: /api/repartitions/list
    Liste paginée des enregistrements de répartitions.
    """
    
    # Optimisation : Charger les données Site
    queryset = Repartition.objects.all().select_related('site').order_by('-repartition_date')
    
    # Serializer
    serializer_class = RepartitionSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = RepartitionListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Site, Catégorie, Date/Montant
    filterset_fields = {
        'site': ['exact'],
        'category': ['exact'],
        'repartition_date': ['exact', 'gte', 'lte'], 
        'montant': ['gte', 'lte'], 
    }
    
    # Recherche textuelle (par détails, nom de site)
    search_fields = ['details', 'site__name']
    
    # Tri possible
    ordering_fields = ['repartition_date', 'montant', 'category', 'site__name']
    ordering = ['-repartition_date']