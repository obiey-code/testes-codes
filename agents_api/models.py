# agents_api/models.py
from django.db import models
from django.conf import settings 
# settings.AUTH_USER_MODEL est CustomUser de notre app users_api

class Agent(models.Model):
    """
    Modèle représentant un Agent du système (e.g., caissier, superviseur, etc.).
    """
    # Lier l'Agent à un compte utilisateur pour l'authentification
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        primary_key=True,
        verbose_name="Compte Utilisateur Associé"
    )
    agent_code = models.CharField(max_length=20, unique=True, verbose_name="Code Agent")
    hire_date = models.DateField(auto_now_add=True, verbose_name="Date d'Embauche")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ['agent_code']
        
    def __str__(self):
        return f"{self.agent_code} - {self.user.last_name}"