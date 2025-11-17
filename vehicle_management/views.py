# vehicles_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import VehicleType
from .serializers import VehicleTypeSerializer

class VehicleTypeAllPostAPIView(APIView):
    """
    Endpoint: POST /api/vehicle-types/all
    Récupère la liste complète (sans pagination) de tous les types de véhicules.
    """
    # Sécurité : L'utilisateur doit être connecté.
    permission_classes = [permissions.IsAuthenticated] 
    
    def post(self, request, format=None):
        # Récupérer l'ensemble des types de véhicules
        # Si vous vouliez n'inclure que les types actifs, vous utiliseriez : 
        # queryset = VehicleType.objects.filter(is_active=True)
        queryset = VehicleType.objects.all()
        
        # Sérialiser la liste d'objets (many=True)
        serializer = VehicleTypeSerializer(queryset, many=True)
        
        # Retourner les données sérialisées
        return Response(serializer.data, status=status.HTTP_200_OK)