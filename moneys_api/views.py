# moneys_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Money
from .serializers import MoneySerializer

# --- Classe de Pagination ---
class MoneyListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class MoneyListAPIView(generics.ListAPIView):
    """
    API: /api/moneys/list
    Liste paginée des mouvements d'argent.
    """
    
    # Optimisation : Charger les données Caissier, Agent et User
    queryset = Money.objects.all().select_related(
        'caissier', 
        'caissier__agent', 
        'caissier__agent__user'
    ).order_by('-timestamp')
    
    # Serializer
    serializer_class = MoneySerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = MoneyListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Caissier, Type de transaction ou Date
    filterset_fields = {
        'caissier': ['exact'],
        'transaction_type': ['exact'],
        'timestamp': ['exact', 'gte', 'lte', 'date'], # Filtrage par date/période
        'montant': ['gte', 'lte'], # Filtrage par montant min/max
        'currency': ['exact'],
    }
    
    # Recherche textuelle (par notes, matricule caissier)
    search_fields = ['notes', 'caissier__matricule_caissier']
    
    # Tri possible
    ordering_fields = ['timestamp', 'montant', 'transaction_type']
    ordering = ['-timestamp']