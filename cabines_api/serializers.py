# cabines_api/serializers.py
from rest_framework import serializers
from .models import Cabine
# Importation du Serializer du site pour la relation (meilleure pratique)
from sites_api.serializers import SiteSerializer 

class CabineSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Cabine.
    """
    # 1. Utilisation du Serializer du Site pour inclure les détails du site (imbrication)
    # site = SiteSerializer(read_only=True) 
    
    # 2. OU, plus simple pour l'affichage de liste, utiliser un champ SerializerMethodField ou CharField
    site_name = serializers.CharField(source='site.name', read_only=True)

    class Meta:
        model = Cabine
        fields = (
            'id', 'cabine_number', 'site', 'site_name', 'direction', 'is_active'
        )
        read_only_fields = fields