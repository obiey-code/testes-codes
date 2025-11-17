# tarifs_api/serializers.py
from rest_framework import serializers
from .models import Tarif

class TarifSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Tarif.
    """
    # Affichage du libellé du type de véhicule
    vehicle_type_display = serializers.CharField(source='get_vehicle_type_display', read_only=True)
    
    # Affichage du nom du site lié
    site_name = serializers.CharField(source='site.name', read_only=True, allow_null=True)

    class Meta:
        model = Tarif
        fields = (
            'id', 'site', 'site_name', 'vehicle_type', 'vehicle_type_display',
            'montant', 'is_active', 'start_date'
        )
        read_only_fields = fields