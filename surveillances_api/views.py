# surveillances_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Surveillance
from .serializers import SurveillanceSerializer

# --- Classe de Pagination ---
class SurveillanceListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class SurveillanceListAPIView(generics.ListAPIView):
    """
    API: /api/surveillances/list
    Liste paginée des événements de surveillance.
    """
    
    # Optimisation : Charger Equipement, Suiveur, Agent et Site (via Equipement->Cabine->Site)
    queryset = Surveillance.objects.all().select_related(
        'equipement', 
        'suiveur', 
        'suiveur__agent',
        'equipement__cabine', 
        'equipement__cabine__site'
    ).order_by('-surveillance_date')
    
    # Serializer
    serializer_class = SurveillanceSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID d'Équipement, ID de Suiveur, Statut ou Date
    filterset_fields = {
        'equipement': ['exact'],
        'suiveur': ['exact'],
        'status': ['exact'],
        'surveillance_date': ['gte', 'lte', 'date'], 
    }
    
    # Recherche textuelle
    search_fields = ['report', 'equipement__serial_number', 'suiveur__matricule_suiveur']
    
    # Tri possible
    ordering_fields = ['surveillance_date', 'status', 'equipement__serial_number']
    ordering = ['-surveillance_date']