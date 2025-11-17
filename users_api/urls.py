# users_api/urls.py (Mise à jour)
from django.urls import path
from .views import UserListAPIView, UserSaveAPIView

urlpatterns = [
    # API de liste (déjà créée)
    path('list', UserListAPIView.as_view(), name='user-list'),
    
    # Nouvelle API de sauvegarde (Création/Mise à jour)
    path('save', UserSaveAPIView.as_view(), name='user-save'),
    
    # ... autres chemins ...
]