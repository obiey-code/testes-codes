# toll_users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginAPIView, LogoutAPIView, CurrentUserAPIView

# 1. Configuration du Routeur pour le CRUD User
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user') 

urlpatterns = [
    # ---------------------------------------------------
    # Routes d'Authentification (/api/auth/*)
    # ---------------------------------------------------
    path('auth/login', LoginAPIView.as_view(), name='auth-login'),
    path('auth/logout', LogoutAPIView.as_view(), name='auth-logout'),
    path('auth/current-user', CurrentUserAPIView.as_view(), name='auth-current-user'),
    # Note: Les vues update et change-password peuvent être implémentées
    #       en personnalisant UserViewSet ou en ajoutant des vues spécifiques.

    # ---------------------------------------------------
    # Routes CRUD (Générées) (/api/users/*)
    # ---------------------------------------------------
    path('', include(router.urls)), 
]