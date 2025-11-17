# repartitions_api/serializers.py
from rest_framework import serializers
from .models import Repartition

class RepartitionSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Repartition.
    """
    # Affichage du nom du site lié
    site_name = serializers.CharField(source='site.name', read_only=True, allow_null=True)
    
    # Affichage du libellé de la catégorie
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Repartition
        fields = (
            'id', 'repartition_date', 'montant', 'category', 'category_display',
            'details', 'created_at', 'site', 'site_name'
        )
        read_only_fields = fields