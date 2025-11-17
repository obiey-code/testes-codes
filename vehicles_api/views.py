# vehicles_api/views.py
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from .models import VehicleType
from .serializers import VehicleTypeSerializer

class VehicleTypeAllAPIView(generics.ListAPIView):
    """
    API: /api/vehicle-types/all
    Permet de récupérer la liste complète des types de véhicules (sans pagination).
    """
    
    # Récupérer tous les types de véhicules actifs
    queryset = VehicleType.objects.filter(is_active=True).order_by('code')
    
    # Serializer
    serializer_class = VehicleTypeSerializer
    
    # Permissions : Accès uniquement aux utilisateurs authentifiés
    permission_classes = [IsAuthenticated]
    
    # PAS DE PAGINATION
    pagination_class = None 
    
    # Filtrage et Tri
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'code', 'label']
    ordering = ['code']