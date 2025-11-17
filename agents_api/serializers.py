# agents_api/serializers.py
from rest_framework import serializers
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Agent.
    Utilise Source pour récupérer les informations de l'utilisateur lié.
    """
    # Champs tirés du modèle utilisateur lié (via le champ 'user')
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    
    class Meta:
        model = Agent
        fields = (
            'agent_code', 'email', 'first_name', 'last_name', 
            'hire_date', 'is_active'
        )
        # agent_code est la clé primaire dans cette configuration, pas besoin d'id
        read_only_fields = fields