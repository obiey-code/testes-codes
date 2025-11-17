# suiveurs_api/models.py
from django.db import models
from agents_api.models import Agent # Importation du modèle Agent

class Suiveur(models.Model):
    """
    Modèle représentant un Suiveur (Agent de suivi, de monitoring ou de surveillance).
    C'est un rôle spécifique d'un Agent.
    """
    # Lier le Suiveur à un Agent existant
    agent = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Agent Associé (Suiveur)"
    )
    matricule_suiveur = models.CharField(max_length=20, unique=True, verbose_name="Matricule du Suiveur")
    is_field_agent = models.BooleanField(default=True, verbose_name="Est Agent de Terrain")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Suiveur"
        verbose_name_plural = "Suiveurs"
        ordering = ['matricule_suiveur']
        
    def __str__(self):
        return f"Suiveur {self.matricule_suiveur}"