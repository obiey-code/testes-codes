# toll_users/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour les opérations CRUD sur le modèle User.
    Gère le hachage sécurisé du mot de passe lors de la création/mise à jour.
    """
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 
            'role', 'site_uuid', 'is_active', 'date_joined', 'password'
        )
        # Configuration des champs pour la sécurité et la lecture
        read_only_fields = ('date_joined',)
        extra_kwargs = {
            'password': {'write_only': True, 'required': False} # Mdp n'est jamais lu
        } 

    def create(self, validated_data):
        # Utilise la méthode native de Django pour hasher le mot de passe
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Si le mot de passe est présent, le hacher avant la mise à jour
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
            
        return super().update(instance, validated_data)