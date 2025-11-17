# responsables_api/serializers.py
from rest_framework import serializers
from .models import Responsable

class ResponsableSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Responsable, incluant les détails de l'Agent et des Sites.
    """
    # Informations de l'Agent/Utilisateur via les champs liés
    agent_code = serializers.CharField(source='agent.agent_code', read_only=True)
    email = serializers.EmailField(source='agent.user.email', read_only=True)
    first_name = serializers.CharField(source='agent.user.first_name', read_only=True)
    last_name = serializers.CharField(source='agent.user.last_name', read_only=True)
    
    # Affichage des noms des sites gérés (champ Many-to-Many)
    managed_site_names = serializers.SerializerMethodField()

    class Meta:
        model = Responsable
        fields = (
            'matricule_responsable', 'agent_code', 'email', 'first_name', 
            'last_name', 'is_active', 'managed_sites', 'managed_site_names'
        )
        read_only_fields = fields

    def get_managed_site_names(self, obj):
        # Récupère et retourne la liste des noms des sites
        return list(obj.managed_sites.values_list('name', flat=True))