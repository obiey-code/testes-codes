# equipements_api/serializers.py
from rest_framework import serializers
from .models import Equipement

class EquipementSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Equipement.
    """
    # Affichage du libellé du statut au lieu de la clé 'ONLINE'/'OFFLINE'
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    # Informations de la cabine liée
    cabine_number = serializers.CharField(source='cabine.cabine_number', read_only=True, allow_null=True)
    
    # Informations du site via la cabine
    site_name = serializers.CharField(source='cabine.site.name', read_only=True, allow_null=True)

    class Meta:
        model = Equipement
        fields = (
            'id', 'serial_number', 'name', 'status', 'status_display', 
            'last_check', 'is_active', 'cabine', 'cabine_number', 'site_name'
        )
        read_only_fields = fields