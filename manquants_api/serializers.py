# manquants_api/serializers.py
from rest_framework import serializers
from .models import Manquant

class ManquantSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Manquant.
    """
    # Affichage du matricule du caissier lié
    matricule_caissier = serializers.CharField(source='caissier.matricule_caissier', read_only=True, allow_null=True)
    
    # Affichage du nom de l'utilisateur lié (via Caissier -> Agent -> User)
    caissier_last_name = serializers.CharField(source='caissier.agent.user.last_name', read_only=True, allow_null=True)


    class Meta:
        model = Manquant
        fields = (
            'id', 'date_manquant', 'montant', 'justification', 
            'is_resolved', 'caissier', 'matricule_caissier', 'caissier_last_name'
        )
        read_only_fields = fields