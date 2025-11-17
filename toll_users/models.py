# toll_users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modèle d'utilisateur personnalisé héritant de AbstractUser.
    Inclut des champs spécifiques comme le rôle pour la gestion des accès.
    """
    
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('responsable', 'Responsable'),
        ('receveur', 'Receveur'),
        ('caissier', 'Caissier'),
        # Ajoutez ici d'autres rôles basés sur vos entités (suiveur, superviseur, etc.)
    )
    
    role = models.CharField(
        max_length=50, 
        choices=ROLE_CHOICES, 
        default='receveur',
        verbose_name="Rôle de l'utilisateur"
    )
    
    # Champ supposé pour le filtrage par site/localisation, basé sur l'API blueprint.
    site_uuid = models.CharField(
        max_length=100, 
        null=True, 
        blank=True,
        verbose_name="UUID du site d'affectation"
    )

    # -----------------------------------------------------------
    # Correction des conflits de related_name
    # -----------------------------------------------------------
    # Permet de coexister avec d'autres modèles d'utilisateur personnalisés (comme users_api.CustomUser)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="toll_users_groups_set", # <--- NOM UNIQUE
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="toll_users_permissions_set", # <--- NOM UNIQUE
        related_query_name="user",
    )
    # -----------------------------------------------------------

    class Meta:
        verbose_name = "Utilisateur du Péage"
        verbose_name_plural = "Utilisateurs du Péage"
        
    def __str__(self):
        return f"{self.username} ({self.role})"