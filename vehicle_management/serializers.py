# vehicles_api/serializers.py
from rest_framework import serializers
from .models import VehicleType

class VehicleTypeSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour la conversion du modèle VehicleType en JSON.
    """
    class Meta:
        model = VehicleType
        fields = ('id', 'name', 'code', 'description')