# auth_api/urls.py

from django.urls import path
from .views import LoginAPIView

# Le préfixe de cet app sera '/api/auth/' défini dans le urls.py du projet principal
urlpatterns = [
    # URL: /api/auth/login
    path('login', LoginAPIView.as_view(), name='login'),
    
    # Ajoutez ici les autres URLs de l'authentification, par exemple :
    # path('logout', LogoutAPIView.as_view(), name='logout'),
    # path('current-user', CurrentUserAPIView.as_view(), name='current-user'),
]