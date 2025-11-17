# ames_api/serializers.py
from rest_framework import serializers
from .models import AME

class AMESerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle AME.
    """
    class Meta:
        model = AME
        fields = (
            'id', 'code', 'name', 'contact_person', 'is_active', 'created_at'
        )
        read_only_fields = fields