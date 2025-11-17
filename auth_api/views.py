# auth_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate # Fonction standard de Django pour l'authentification
from rest_framework.authtoken.models import Token # Pour gérer les tokens d'authentification

from .serializers import LoginSerializer, AuthTokenSerializer

class LoginAPIView(APIView):
    """
    API pour la connexion des utilisateurs.
    URL: /api/auth/login
    Méthode: POST
    """
    
    # 1. Utiliser le Serializer pour la validation des données entrantes
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        # 2. Valider les données
        if not serializer.is_valid():
            # Retourne 400 Bad Request si la validation échoue
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 3. Récupérer les données validées
        email = serializer.validated_data.get('email').lower()
        password = serializer.validated_data.get('password')

        # 4. Authentifier l'utilisateur
        # NOTE : Vous devrez configurer votre modèle utilisateur pour utiliser l'email comme identifiant.
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # 5. Créer ou récupérer le Token d'authentification
            # (Utilisation de DRF Token Authentication pour la simplicité)
            token, created = Token.objects.get_or_create(user=user)
            
            # 6. Retourner la réponse 200 Successful operation
            response_serializer = AuthTokenSerializer({'token': token.key})
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        else:
            # 7. Retourner 401 Unauthorized en cas d'échec d'authentification
            # (C'est un pattern commun pour la sécurité)
            return Response(
                {"detail": "Identifiants invalides."},
                status=status.HTTP_401_UNAUTHORIZED
            )