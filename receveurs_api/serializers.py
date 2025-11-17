# receveurs_api/serializers.py
from rest_framework import serializers
from .models import Receveur

class ReceveurSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Receveur, incluant les détails de l'Agent et de l'Utilisateur.
    """
    # Informations de l'Agent/Utilisateur via les champs liés
    agent_code = serializers.CharField(source='agent.agent_code', read_only=True)
    email = serializers.EmailField(source='agent.user.email', read_only=True)
    first_name = serializers.CharField(source='agent.user.first_name', read_only=True)
    last_name = serializers.CharField(source='agent.user.last_name', read_only=True)

    class Meta:
        model = Receveur
        fields = (
            'matricule_receveur', 'agent_code', 'email', 'first_name', 
            'last_name', 'is_supervisor', 'is_active'
        )
        read_only_fields = fields