from django.db import models

# Create your models here.
# caissiers_api/models.py
from django.db import models
from agents_api.models import Agent # Importation du modèle Agent

class Caissier(models.Model):
    """
    Modèle représentant un Caissier. C'est un rôle spécifique d'un Agent.
    """
    # Lier le Caissier à un Agent via une relation OneToOne ou ForeignKey
    # Utilisons OneToOne si un Agent est soit un Caissier, soit un autre type d'Agent, mais pas les deux en même temps.
    agent = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Agent Associé"
    )
    matricule_caissier = models.CharField(max_length=20, unique=True, verbose_name="Matricule du Caissier")
    is_trained = models.BooleanField(default=True, verbose_name="Est Formé")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Caissier"
        verbose_name_plural = "Caissiers"
        ordering = ['matricule_caissier']
        
    def __str__(self):
        return f"Caissier {self.matricule_caissier}"