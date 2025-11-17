# user_management/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSaveSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour la création et la mise à jour des utilisateurs (/api/users/save).
    Gère la logique de hachage du mot de passe.
    """
    # Champ ID optionnel (requis pour la mise à jour, absent pour la création)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def create(self, validated_data):
        # Logique de création (hachage du mot de passe)
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        # Logique de mise à jour
        password = validated_data.pop('password', None)
        validated_data.pop('id', None) 
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance