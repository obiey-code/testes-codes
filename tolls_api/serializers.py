# tolls_api/serializers.py
from rest_framework import serializers
from .models import TollSubscriber

class TollSubscriberSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle TollSubscriber.
    """
    # Champ calculé pour afficher l'email de l'utilisateur lié
    user_email = serializers.EmailField(source='user.email', read_only=True, allow_null=True)

    class Meta:
        model = TollSubscriber
        fields = (
            'id', 'subscriber_number', 'registration_plate', 'balance', 
            'is_active', 'user_email', 'created_at'
        )
        read_only_fields = fields