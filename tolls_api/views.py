# tolls_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import TollSubscriber
from .serializers import TollSubscriberSerializer

# --- Classe de Pagination (Réutilisation) ---
class TollListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class TollSubscriberListAPIView(generics.ListAPIView):
    """
    API: /api/toll-subscribers/list
    Liste paginée des abonnés au péage.
    """
    
    # Récupérer la requête de base
    queryset = TollSubscriber.objects.filter(is_active=True).select_related('user').order_by('subscriber_number')
    
    # Serializer
    serializer_class = TollSubscriberSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = TollListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Permet la recherche par numéro, plaque ou email utilisateur (via le champ lié)
    search_fields = ['subscriber_number', 'registration_plate', 'user__email']
    
    # Tri possible
    ordering_fields = ['id', 'subscriber_number', 'registration_plate', 'balance']
    ordering = ['subscriber_number']