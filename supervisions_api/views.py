# supervisions_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .models import Supervision
from .serializers import SupervisionSerializer

# --- Classe de Pagination ---
class SupervisionListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class SupervisionListAPIView(generics.ListAPIView):
    """
    API: /api/supervisions/list
    Liste paginée des événements de supervision.
    """
    
    # Optimisation : Charger Responsable (et son Agent/User), Site, et Cabine
    queryset = Supervision.objects.all().select_related(
        'responsable', 
        'responsable__agent', 
        'responsable__agent__user',
        'site', 
        'cabine'
    ).order_by('-supervision_date')
    
    # Serializer
    serializer_class = SupervisionSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtrage précis : par ID de Responsable, Site, Cabine, Grade, Date
    filterset_fields = {
        'responsable': ['exact'],
        'site': ['exact'],
        'cabine': ['exact'],
        'grade': ['exact'],
        'is_closed': ['exact'],
        'supervision_date': ['gte', 'lte', 'date'], 
    }
    
    # Recherche textuelle
    search_fields = ['summary', 'responsable__matricule_responsable', 'site__name', 'cabine__cabine_number']
    
    # Tri possible
    ordering_fields = ['supervision_date', 'grade', 'is_closed']
    ordering = ['-supervision_date']