# users_api/views.py
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView # Utilisez APIView pour la logique Création/Mise à jour unifiée



# --- Classe de Pagination Personnalisée ---
class StandardResultsSetPagination(PageNumberPagination):
    """
    Définit le style de pagination pour les listes.
    Permet de définir la taille de la page (size) via un paramètre de requête.
    """
    page_size = 10
    page_size_query_param = 'size'  # Permet ?size=20
    max_page_size = 100

# --- Vue pour l'API de Liste ---
class UserListAPIView(generics.ListAPIView):
    """
    API: /api/users/list
    Permet de récupérer la liste des utilisateurs avec filtrage et pagination.
    """
    
    # 1. Requête de base pour les données
    queryset = CustomUser.objects.all().order_by('email')
    
    # 2. Serializer pour formater les données de sortie
    serializer_class = UserSerializer
    
    # 3. Permissions : Seuls les utilisateurs authentifiés peuvent accéder à cette liste
    permission_classes = [IsAuthenticated]
    
    # 4. Pagination : Utiliser notre classe de pagination personnalisée
    pagination_class = StandardResultsSetPagination
    
    # 5. Filtrage et Recherche : Définir comment l'utilisateur peut filtrer les données
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Champs sur lesquels la recherche sera effectuée (via ?search=...)
    search_fields = ['email', 'first_name', 'last_name']
    
    # Champs sur lesquels le tri sera possible (via ?ordering=...)
    ordering_fields = ['id', 'email', 'last_name']
    
    # Tri par défaut
    ordering = ['email']









class UserSaveAPIView(APIView):
    """
    API: /api/users/save
    Permet de créer un nouvel utilisateur ou de mettre à jour un utilisateur existant (upsert).
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user_id = data.get('id')

        # Si un ID est fourni, nous cherchons l'utilisateur à mettre à jour
        if user_id:
            try:
                # 1. Récupérer l'utilisateur existant
                instance = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return Response(
                    {"detail": "Utilisateur non trouvé pour la mise à jour."}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # 2. Initialiser le Serializer avec l'instance existante
            serializer = self.serializer_class(instance, data=data, partial=True) # partial=True pour la MAJ partielle
            
        # Sinon, c'est une création
        else:
            # 1. Initialiser le Serializer sans instance
            serializer = self.serializer_class(data=data)
        
        
        # 3. Valider et Sauvegarder
        if serializer.is_valid():
            user_instance = serializer.save()
            
            # 4. Retourner la réponse avec les données du nouvel utilisateur/mis à jour
            return Response(
                self.serializer_class(user_instance).data, 
                status=status.HTTP_200_OK
            )
        
        # 5. Retourner les erreurs de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)