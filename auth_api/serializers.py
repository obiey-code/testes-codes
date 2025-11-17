# auth_api/serializers.py

from rest_framework import serializers

# 1. Serializer pour l'entrée (Request Body) de l'API de connexion
class LoginSerializer(serializers.Serializer):
    """
    Définit les champs requis pour la connexion : email et password.
    Utilisé pour la validation des données entrantes.
    """
    # L'email est un 'object' dans la spec, mais en pratique, c'est généralement traité comme un string
    # représentant une adresse email.
    email = serializers.EmailField(required=True) 
    password = serializers.CharField(required=True, write_only=True) # write_only pour ne pas l'inclure en sortie

# 2. Serializer pour la sortie (Response Body) de l'API de connexion
class AuthTokenSerializer(serializers.Serializer):
    """
    Définit le format de la réponse après une connexion réussie.
    """
    token = serializers.CharField()