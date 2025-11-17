# site_management/serializers.py
from rest_framework import serializers
from .models import Site # Importe le modèle Site que vous avez défini

class SiteSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour la conversion du modèle Site en JSON.
    Définit les champs qui seront inclus dans la réponse de l'API /api/sites/all.
    """
    class Meta:
        model = Site
        # Choisissez les champs à exposer. Ce sont les données qui seront renvoyées
        fields = ('id', 'name', 'code', 'is_active') 
        # Si vous n'utilisez ces données que pour la lecture (comme pour un "all list"),
        # vous pouvez également spécifier des champs en lecture seule si nécessaire.