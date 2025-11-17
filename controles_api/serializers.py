# controles_api/serializers.py
from rest_framework import serializers
from .models import Controle

class ControleSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Controle.
    Affiche les informations essentielles des entités liées.
    """
    # Affichage du nom de l'agent contrôleur
    agent_code = serializers.CharField(source='agent.agent_code', read_only=True, allow_null=True)
    agent_name = serializers.CharField(source='agent.user.last_name', read_only=True, allow_null=True)
    
    # Affichage du nom du site contrôlé
    site_name = serializers.CharField(source='site.name', read_only=True, allow_null=True)
    
    # Affichage du libellé du résultat au lieu de la clé 'OK'/'KO'
    result_display = serializers.CharField(source='get_result_display', read_only=True)

    class Meta:
        model = Controle
        fields = (
            'id', 'control_date', 'agent', 'agent_code', 'agent_name', 
            'site', 'site_name', 'result', 'result_display', 'notes'
        )
        read_only_fields = fields