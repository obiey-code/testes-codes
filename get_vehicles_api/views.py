# get_vehicles_api/views.py

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
# Importe les modèles depuis ce même package :
from .models import VehicleType, Vehicle 
# Importe les sérialiseurs (assurez-vous d'avoir créé serializers.py !)
from .serializers import VehicleTypeSerializer, VehicleSerializer 

# VUE 1 : POST /api/vehicle-types/all
class VehicleTypeAllPostAPIView(APIView): 
    """ Vue qui doit être importée dans urls.py """
    permission_classes = [permissions.IsAuthenticated] 
    
    def post(self, request, format=None):
        queryset = VehicleType.objects.all()
        serializer = VehicleTypeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# VUE 2 : GET /api/vehicles/{id}
class VehicleRetrieveAPIView(RetrieveAPIView): 
    """ Vue qui doit être importée dans urls.py """
    queryset = Vehicle.objects.all() 
    serializer_class = VehicleSerializer
    lookup_field = 'pk' 
    permission_classes = [permissions.IsAuthenticated]