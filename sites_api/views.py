# sites_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Site
from .serializers import SiteSerializer

# --- Classe de Pagination (Pour la réutilisation) ---
# En pratique, ceci serait dans un package commun ou copié ici
class SiteListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class SiteListAPIView(generics.ListAPIView):
    """
    API: /api/sites/list
    Permet de récupérer la liste des sites avec filtrage et pagination.
    """
    
    # 1. Requête de base pour les données (on ne prend que les sites actifs)
    queryset = Site.objects.filter(is_active=True).order_by('name')
    
    # 2. Serializer pour formater les données de sortie
    serializer_class = SiteSerializer
    
    # 3. Permissions : Seuls les utilisateurs authentifiés peuvent accéder
    permission_classes = [IsAuthenticated]
    
    # 4. Pagination
    pagination_class = SiteListPagination
    
    # 5. Filtrage et Recherche
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code'] # Permet de rechercher par nom ou par code
    ordering_fields = ['id', 'name', 'code', 'created_at']
    ordering = ['name']



    # sites_api/views.py

from rest_framework import generics, filters
# ... autres imports ...

# ... (Le code de SiteListPagination et SiteListAPIView reste le même) ...

# --- Vue pour l'API de Liste Complète ---
class SiteAllAPIView(generics.ListAPIView):
    """
    API: /api/sites/all
    Permet de récupérer la liste complète des sites (sans pagination).
    Idéal pour les listes déroulantes, etc.
    """
    
    # 1. Requête de base pour les données
    # Nous utilisons la même requête que pour /list pour garantir la cohérence
    queryset = Site.objects.filter(is_active=True).order_by('name')
    
    # 2. Serializer pour formater les données de sortie
    serializer_class = SiteSerializer
    
    # 3. Permissions
    permission_classes = [IsAuthenticated]
    
    # 4. PAS DE PAGINATION : Le point crucial !
    pagination_class = None 
    
    # 5. Filtrage (La recherche textuelle est souvent inutile pour une liste 'all')
    # Nous gardons uniquement l'Ordering pour garantir un ordre alphabétique
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['name']