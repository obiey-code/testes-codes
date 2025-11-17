# supervisions_api/serializers.py
from rest_framework import serializers
from .models import Supervision

class SupervisionSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Supervision.
    """
    # Affichage du grade en toutes lettres
    grade_display = serializers.CharField(source='get_grade_display', read_only=True)
    
    # Informations des entités liées
    matricule_responsable = serializers.CharField(source='responsable.matricule_responsable', read_only=True, allow_null=True)
    site_name = serializers.CharField(source='site.name', read_only=True, allow_null=True)
    cabine_number = serializers.CharField(source='cabine.cabine_number', read_only=True, allow_null=True)


    class Meta:
        model = Supervision
        fields = (
            'id', 'supervision_date', 'grade', 'grade_display', 'summary', 'is_closed', 
            'responsable', 'matricule_responsable', 'site', 'site_name', 'cabine', 'cabine_number'
        )
        read_only_fields = fields