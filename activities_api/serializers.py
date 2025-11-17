# activities_api/serializers.py
from rest_framework import serializers
from .models import Activity
from users_api.serializers import UserSerializer # Réutilisation du Serializer d'utilisateur

# Serializer simple pour l'utilisateur dans l'activité (pour ne pas retourner TOUTES les infos utilisateur)
class ActivityUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Activity.
    Affiche l'utilisateur associé à l'activité.
    """
    # Utiliser le Serializer simplifié pour afficher l'utilisateur au lieu de son ID seulement
    user = ActivityUserSerializer(read_only=True) 

    class Meta:
        model = Activity
        fields = ('id', 'user', 'title', 'details', 'timestamp')
        read_only_fields = fields