# moneys_api/models.py
from django.db import models
from caissiers_api.models import Caissier # Le caissier concerné par le mouvement

class Money(models.Model):
    """
    Modèle représentant un Mouvement d'Argent (e.g., remise de fonds, transfert).
    """
    caissier = models.ForeignKey(
        Caissier,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Caissier Opérateur"
    )
    transaction_type = models.CharField(
        max_length=50,
        choices=[
            ('REMISE', 'Remise de Fonds'), 
            ('VERSEMENT', 'Versement'), 
            ('SORTIE', 'Sortie de Caisse')
        ],
        verbose_name="Type de Transaction"
    )
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")
    currency = models.CharField(max_length=3, default='XOF', verbose_name="Devise (ISO 4217)")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Horodatage")
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Mouvement d'Argent"
        verbose_name_plural = "Mouvements d'Argent"
        ordering = ['-timestamp'] # Du plus récent au plus ancien
        
    def __str__(self):
        return f"{self.transaction_type} de {self.montant} {self.currency} par {self.caissier.matricule_caissier if self.caissier else 'N/A'}"