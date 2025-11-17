# vehicles_api/serializers.py
from rest_framework import serializers
from .models import VehicleType, Vehicle

# Sérialiseur pour le type de véhicule (si vous ne l'aviez pas déjà)
class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('id', 'name', 'code', 'description') 

# NOUVEAU SÉRIALISEUR : VehicleSerializer
class VehicleSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Vehicle.
    Affiche les détails du type de véhicule.
    """
    # Ce champ sera sérialisé en utilisant le VehicleTypeSerializer
    vehicle_type = VehicleTypeSerializer(read_only=True) 
    
    # Pour permettre la création/mise à jour, il est préférable d'avoir un champ ID
    # vers VehicleType qui sera utilisé lors de la création/mise à jour.
    vehicle_type_id = serializers.PrimaryKeyRelatedField(
        queryset=VehicleType.objects.all(), 
        source='vehicle_type', 
        write_only=True
    )

    class Meta:
        model = Vehicle
        fields = (
            'id', 
            'registration_number', 
            'vehicle_type',       # Sortie (GET)
            'vehicle_type_id',    # Entrée (POST/PUT)
            'owner_name', 
            'is_active'
        )