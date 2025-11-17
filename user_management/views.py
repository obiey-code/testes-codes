# user_management/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSaveSerializer

User = get_user_model()

class UserSaveAPIView(APIView):
    """
    Gère la création et la mise à jour d'un utilisateur via un seul endpoint POST.
    
    Requis : Seuls les utilisateurs administrateurs peuvent manipuler d'autres comptes.
    """
    # Recommandation : Limitez l'accès à ceux qui ont les permissions de gérer les utilisateurs
    permission_classes = [permissions.IsAdminUser] 
    
    def post(self, request, format=None):
        # 1. Tenter de récupérer l'ID
        user_id = request.data.get('id')
        
        if user_id:
            # --- SCÉNARIO DE MISE À JOUR (UPDATE) ---
            try:
                # Récupérer l'utilisateur existant
                instance = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response(
                    {"detail": f"L'utilisateur avec ID {user_id} est introuvable pour la mise à jour."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Sérialiseur en mode mise à jour (l'instance est fournie)
            serializer = UserSaveSerializer(instance, data=request.data, partial=True)
            
        else:
            # --- SCÉNARIO DE CRÉATION (CREATE) ---
            # Sérialiseur en mode création (pas d'instance fournie)
            serializer = UserSaveSerializer(data=request.data)

        # 2. Validation et Sauvegarde
        if serializer.is_valid():
            user_instance = serializer.save()
            
            # 3. Réponse
            action = "mis à jour" if user_id else "créé"
            
            # Nous resérialisons l'instance pour garantir que le mot de passe n'est pas inclus dans la réponse
            response_data = UserSaveSerializer(user_instance).data
            
            return Response(
                {
                    "detail": f"Utilisateur '{user_instance.username}' {action} avec succès.",
                    "user": response_data
                },
                status=status.HTTP_200_OK # 200 OK est commun pour une opération de 'save' réussie
            )
        
        # 4. Erreur de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)