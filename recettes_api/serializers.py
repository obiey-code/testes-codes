# recettes_api/serializers.py
from rest_framework import serializers
from .models import Recette

class RecetteSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Recette.
    """
    # Affichage en toutes lettres de la méthode de paiement
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    
    # Informations du Caissier
    matricule_caissier = serializers.CharField(source='caissier.matricule_caissier', read_only=True, allow_null=True)
    
    # Informations de la Cabine et du Site
    cabine_number = serializers.CharField(source='cabine.cabine_number', read_only=True, allow_null=True)
    site_name = serializers.CharField(source='site.name', read_only=True, allow_null=True)


    class Meta:
        model = Recette
        fields = (
            'id', 'transaction_ref', 'montant', 'payment_method', 'payment_method_display',
            'timestamp', 'caissier', 'matricule_caissier', 'cabine', 'cabine_number',
            'site', 'site_name'
        )
        read_only_fields = fields