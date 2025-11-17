# responsables_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Responsable
from .serializers import ResponsableSerializer

# --- Classe de Pagination ---
class ResponsableListPagination(PageNumberPagination):
    page_size = 20 
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class ResponsableListAPIView(generics.ListAPIView):
    """
    API: /api/responsables/list
    Liste paginée des responsables.
    """
    
    # Optimisation : select_related pour Agent/User (ForeignKey/OneToOne)
    # et prefetch_related pour managed_sites (ManyToMany)
    queryset = Responsable.objects.filter(is_active=True)\
        .select_related('agent', 'agent__user')\
        .prefetch_related('managed_sites')\
        .order_by('matricule_responsable')
    
    # Serializer
    serializer_class = ResponsableSerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = ResponsableListPagination
    
    # Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Recherche par matricule, code agent, email, nom, ou nom de site géré
    search_fields = [
        'matricule_responsable', 
        'agent__agent_code', 
        'agent__user__email', 
        'agent__user__last_name',
        'managed_sites__name' # Permet de chercher un responsable par le nom d'un de ses sites
    ]
    
    # Tri possible
    ordering_fields = ['matricule_responsable', 'agent__user__last_name']
    ordering = ['matricule_responsable']