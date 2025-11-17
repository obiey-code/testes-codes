# controles_api/models.py
from django.db import models
from agents_api.models import Agent # L'agent qui effectue le contrôle
from sites_api.models import Site # Le site où le contrôle est effectué

class Controle(models.Model):
    """
    Modèle représentant un événement de Contrôle (e.g., contrôle de caisse, audit).
    """
    agent = models.ForeignKey(
        Agent,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Agent Contrôleur"
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Site Contrôlé"
    )
    control_date = models.DateTimeField(verbose_name="Date et Heure du Contrôle", auto_now_add=True)
    result = models.CharField(
        max_length=20,
        choices=[('OK', 'Conforme'), ('KO', 'Non Conforme'), ('PARTIAL', 'Partiellement Conforme')],
        default='OK',
        verbose_name="Résultat"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Notes / Commentaires")
    
    class Meta:
        verbose_name = "Contrôle"
        verbose_name_plural = "Contrôles"
        ordering = ['-control_date'] # Du plus récent au plus ancien
        
    def __str__(self):
        return f"Contrôle du {self.control_date.strftime('%Y-%m-%d %H:%M')} par {self.agent.agent_code if self.agent else 'Inconnu'}"