# receveurs_api/models.py
from django.db import models
from agents_api.models import Agent # Importation du modèle Agent

class Receveur(models.Model):
    """
    Modèle représentant un Receveur (responsable de la réception des fonds/audits).
    C'est un rôle spécifique d'un Agent.
    """
    # Lier le Receveur à un Agent existant
    agent = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Agent Associé (Receveur)"
    )
    matricule_receveur = models.CharField(max_length=20, unique=True, verbose_name="Matricule du Receveur")
    is_supervisor = models.BooleanField(default=False, verbose_name="Est Superviseur")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Receveur"
        verbose_name_plural = "Receveurs"
        ordering = ['matricule_receveur']
        
    def __str__(self):
        return f"Receveur {self.matricule_receveur}"