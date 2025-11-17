# users_api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Nous créons ici une extension du modèle utilisateur de base de Django
class CustomUser(AbstractUser):
    # Ajout d'un champ spécifique à notre application
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # Rendre l'email obligatoire et unique
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'email'  # Utiliser l'email pour la connexion
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email