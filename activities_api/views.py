# activities_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

# Nous avons besoin d'un package pour le filtrage par champs d'entités liés
from django_filters.rest_framework import DjangoFilterBackend 

from .models import Activity
from .serializers import ActivitySerializer

# Installation nécessaire : pip install django-filter
# N'oubliez pas d'ajouter 'django_filters' à INSTALLED_APPS dans settings.py

# --- Classe de Pagination ---
class ActivityListPagination(PageNumberPagination):
    page_size = 20 # Peut-être plus pour les logs d'activité
    page_size_query_param = 'size'
    max_page_size = 200

# --- Vue pour l'API de Liste ---
class ActivityListAPIView(generics.ListAPIView):
    """
    API: /api/activities/list
    Liste paginée des activités.
    Supporte la recherche et le filtrage (par titre, par date, par utilisateur).
    """
    
    # Récupérer la requête de base
    queryset = Activity.objects.all().select_related('user') # Optimisation : charger les données utilisateur en même temps
    
    # Serializer
    serializer_class = ActivitySerializer
    
    # Permissions
    permission_classes = [IsAuthenticated]
    
    # Pagination
    pagination_class = ActivityListPagination
    
    # Filtrage et Recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Utilisation de DjangoFilterBackend pour le filtrage précis :
    # 'title' : Filtrage exact ou partiel
    # 'timestamp' : Filtrage par date (e.g., timestamp__gte pour "greater than or equal")
    # 'user__id' : Filtrage par ID d'utilisateur
    filterset_fields = {
        'timestamp': ['gte', 'lte', 'date'], # Permet de filtrer entre deux dates ou une date précise
        'title': ['icontains'], # Recherche insensible à la casse dans le titre
        'user': ['exact'] # Filtrage par l'ID exact de l'utilisateur
    }
    
    # Recherche textuelle (similaire à DjangoFilterBackend, mais plus large)
    search_fields = ['title', 'details', 'user__email']
    
    # Tri par défaut (du plus récent au plus ancien)
    ordering = ['-timestamp']