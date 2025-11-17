# toll_users/views.py

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token 

from .models import User
from .serializers import UserSerializer

# -----------------------------------------------------------
# Vues d'Authentification (Basées sur /api/auth/*)
# -----------------------------------------------------------

class LoginAPIView(ObtainAuthToken):
    """ 
    POST /api/auth/login : 
    Gère la connexion utilisateur. En cas de succès, retourne le Bearer Token.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Récupère ou crée le jeton
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key, 
            'username': user.username,
            'user_id': user.pk, 
            'email': user.email,
            'role': user.role,
        }, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    """ 
    POST /api/auth/logout :
    Déconnexion utilisateur sécurisée en supprimant le jeton Bearer associé. 
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Supprime le jeton lié à l'utilisateur authentifié
            request.user.auth_token.delete()
        except:
            # Si le jeton n'existe pas (déjà déconnecté), l'ignorer
            pass 
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)

class CurrentUserAPIView(APIView):
    """
    GET /api/auth/current-user :
    Retourne les informations de l'utilisateur actuellement connecté (via Bearer Token).
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        # Supprime le champ 'password' avant d'envoyer la réponse
        data = serializer.data
        data.pop('password', None) 
        return Response(data)

# -----------------------------------------------------------
# Vues CRUD (Basées sur /api/users/)
# -----------------------------------------------------------

class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet pour gérer les opérations CRUD complètes sur le modèle User.
    Routes générées :
    - GET/POST /api/users/ (List/Create)
    - GET/PUT/PATCH/DELETE /api/users/{pk}/ (Retrieve/Update/Delete)
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] # Toutes les opérations CRUD nécessitent le Bearer Token

    # Logique pour implémenter les filtres et la pagination spécifiques de /api/users/list
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Exemple de filtrage basé sur des paramètres d'URL (ou data si vous utilisez POST)
        first_name = self.request.query_params.get('first_name', None)
        role = self.request.query_params.get('role', None)
        
        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)
        if role:
            queryset = queryset.filter(role=role)
            
        # DRF gère nativement la pagination si elle est configurée globalement
        return queryset