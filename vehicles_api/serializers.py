# vehicles_api/serializers.py
from rest_framework import serializers
from .models import VehicleType

class VehicleTypeSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle VehicleType.
    """
    class Meta:
        model = VehicleType
        fields = ('id', 'label', 'code', 'description', 'is_active')
        read_only_fields = ('code',) # Le code est souvent généré ou fixe