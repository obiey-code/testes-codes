# responsables_api/models.py
from django.db import models
from agents_api.models import Agent # Le responsable est un Agent
from sites_api.models import Site # Le responsable gère des Sites

class Responsable(models.Model):
    """
    Modèle représentant un Responsable (Superviseur ou Directeur).
    C'est un rôle spécifique d'un Agent.
    """
    # Lier le Responsable à un Agent
    agent = models.OneToOneField(
        Agent,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Agent Associé (Responsable)"
    )
    matricule_responsable = models.CharField(max_length=20, unique=True, verbose_name="Matricule du Responsable")
    
    # Relation Many-to-Many : Un responsable peut gérer plusieurs sites
    managed_sites = models.ManyToManyField(
        Site,
        blank=True,
        verbose_name="Sites Gérés"
    )
    
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        ordering = ['matricule_responsable']
        
    def __str__(self):
        return f"Responsable {self.matricule_responsable}"