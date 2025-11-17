# surveillances_api/models.py
from django.db import models
from equipements_api.models import Equipement # L'équipement surveillé
from suiveurs_api.models import Suiveur # Le suiveur qui effectue la tâche

class Surveillance(models.Model):
    """
    Modèle représentant un événement de Surveillance ou de maintenance préventive.
    """
    equipement = models.ForeignKey(
        Equipement,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Équipement Surveillé"
    )
    suiveur = models.ForeignKey(
        Suiveur,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Suiveur Responsable"
    )
    surveillance_date = models.DateTimeField(verbose_name="Date et Heure de Surveillance", auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('NORMAL', 'Normal'), ('ANOMALY', 'Anomalie'), ('RESOLVED', 'Résolu')],
        default='NORMAL',
        verbose_name="Statut"
    )
    report = models.TextField(blank=True, null=True, verbose_name="Rapport d'Observation")
    
    class Meta:
        verbose_name = "Surveillance"
        verbose_name_plural = "Surveillances"
        ordering = ['-surveillance_date'] # Du plus récent au plus ancien
        
    def __str__(self):
        equipement_sn = self.equipement.serial_number if self.equipement else 'N/A'
        return f"Surveillance de {equipement_sn} le {self.surveillance_date.strftime('%Y-%m-%d %H:%M')}"