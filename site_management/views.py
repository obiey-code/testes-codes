# site_management/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Site
from .serializers import SiteSerializer

class SiteAllPostAPIView(APIView):
    """
    Endpoint: POST /api/sites/all
    Récupère la liste complète (sans pagination) des Sites actifs.
    
    NOTE: Utilise la méthode POST pour être conforme à la spécification de l'utilisateur,
    même si la requête n'a pas besoin de corps.
    """
    # Sécurité : L'utilisateur doit être connecté.
    permission_classes = [permissions.IsAuthenticated] 
    
    def post(self, request, format=None):
        # 1. Le corps de la requête (request.data) est ignoré ici car votre spécification 
        # indique un corps vide, mais il pourrait être utilisé pour des filtres POST ultérieurs.
        
        # 2. Récupérer le QuerySet : tous les sites actifs
        # Nous pouvons ajouter des filtres basés sur request.data ici si nécessaire.
        queryset = Site.objects.filter(is_active=True)
        
        # 3. Sérialiser la totalité du QuerySet
        # L'argument `many=True` indique à DRF qu'il s'agit d'une liste d'objets à sérialiser.
        serializer = SiteSerializer(queryset, many=True)
        
        # 4. Retourner la liste des sites
        return Response(serializer.data, status=status.HTTP_200_OK)