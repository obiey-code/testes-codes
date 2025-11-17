# sites_api/serializers.py
from rest_framework import serializers
from .models import Site

class SiteSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Site.
    """
    class Meta:
        model = Site
        # Les champs que l'API va exposer
        fields = ('id', 'name', 'code', 'is_active', 'created_at')
        read_only_fields = ('created_at',)