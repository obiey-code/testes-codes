# surveillances_api/serializers.py
from rest_framework import serializers
from .models import Surveillance

class SurveillanceSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Surveillance.
    Affiche les informations essentielles des entités liées.
    """
    # Affichage du statut en toutes lettres
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    # Informations de l'équipement surveillé (numéro de série)
    equipement_serial = serializers.CharField(source='equipement.serial_number', read_only=True, allow_null=True)
    
    # Informations du suiveur (matricule)
    suiveur_matricule = serializers.CharField(source='suiveur.matricule_suiveur', read_only=True, allow_null=True)
    
    # Informations du site via Equipement -> Cabine -> Site
    site_name = serializers.CharField(source='equipement.cabine.site.name', read_only=True, allow_null=True)


    class Meta:
        model = Surveillance
        fields = (
            'id', 'surveillance_date', 'status', 'status_display', 'report', 
            'equipement', 'equipement_serial', 'suiveur', 'suiveur_matricule', 'site_name'
        )
        read_only_fields = fields