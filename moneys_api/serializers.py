# moneys_api/serializers.py
from rest_framework import serializers
from .models import Money

class MoneySerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Money (Mouvement d'Argent).
    """
    # Affichage du type de transaction en toutes lettres
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)
    
    # Informations du caissier (via les champs liés)
    matricule_caissier = serializers.CharField(source='caissier.matricule_caissier', read_only=True, allow_null=True)
    caissier_last_name = serializers.CharField(source='caissier.agent.user.last_name', read_only=True, allow_null=True)


    class Meta:
        model = Money
        fields = (
            'id', 'transaction_type', 'transaction_type_display', 'montant', 
            'currency', 'timestamp', 'notes', 'caissier', 
            'matricule_caissier', 'caissier_last_name'
        )
        read_only_fields = fields