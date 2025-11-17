# sites/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Site
from .serializers import SiteSerializer

class SiteViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer le CRUD des Sites.
    Génère : POST/GET /api/sites/, GET/PUT/PATCH/DELETE /api/sites/{pk}/
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]

    # Implémentation de l'endpoint spécifique : GET /api/sites/all
    @action(detail=False, methods=['get'])
    def all(self, request):
        """
        Implémente l'API /api/sites/all demandée.
        Retourne la liste complète de tous les sites sans pagination par défaut.
        """
        # Note: Utiliser all_sites_queryset pour éviter d'appliquer la pagination par défaut
        all_sites_queryset = Site.objects.filter(is_active=True).order_by('name')
        
        # Sérialise le queryset complet
        serializer = self.get_serializer(all_sites_queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Note: Vous pourriez également implémenter /api/sites/list ici en tant qu'action POST
    # @action(detail=False, methods=['post'], url_path='list')
    # def list_sites_filtered(self, request):
    #     # ... Logique de filtrage et pagination personnalisée ...
    #     pass