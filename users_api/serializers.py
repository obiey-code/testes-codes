# users_api/serializers.py (Mise à jour)
from rest_framework import serializers
from django.contrib.auth.hashers import make_password # Pour hacher le mot de passe
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    # ... (le reste du code Meta est identique) ...

    class Meta:
        model = CustomUser
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 
            'phone_number', 'is_active', 'date_joined', 'password' # Inclure password ici
        )
        read_only_fields = ('date_joined', 'is_active')
        extra_kwargs = {
            # Le password n'est accepté qu'en entrée et n'est pas requis pour la MAJ
            'password': {'write_only': True, 'required': False} 
        }

    # Méthode personnalisée pour la CRÉATION (Create)
    def create(self, validated_data):
        # Hachage du mot de passe avant la création
        validated_data['password'] = make_password(validated_data.get('password'))
        # Assurez-vous que l'email est utilisé comme username si non fourni
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email']
        
        return super().create(validated_data)

    # Méthode personnalisée pour la MISE À JOUR (Update)
    def update(self, instance, validated_data):
        # Si le mot de passe est fourni, le hacher et le mettre à jour
        if 'password' in validated_data:
            instance.password = make_password(validated_data.get('password'))
            # Retirer le mot de passe du dictionnaire validé pour que super().update ne le hache pas à nouveau
            validated_data.pop('password', None)
        
        # Le reste des champs est mis à jour par la méthode par défaut
        return super().update(instance, validated_data)