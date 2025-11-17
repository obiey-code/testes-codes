# manquants_api/models.py
from django.db import models
from caissiers_api.models import Caissier # Le caissier concerné par le manquant

class Manquant(models.Model):
    """
    Modèle représentant un Manquant (déficit ou écart) enregistré.
    """
    caissier = models.ForeignKey(
        Caissier,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Caissier Concerné"
    )
    date_manquant = models.DateField(verbose_name="Date du Manquant")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant du Manquant (en devise locale)")
    justification = models.TextField(blank=True, null=True, verbose_name="Justification ou Commentaire")
    is_resolved = models.BooleanField(default=False, verbose_name="Est Résolu")
    
    class Meta:
        verbose_name = "Manquant"
        verbose_name_plural = "Manquants"
        ordering = ['-date_manquant', 'montant'] 
        
    def __str__(self):
        caissier_id = self.caissier.matricule_caissier if self.caissier else 'Inconnu'
        return f"Manquant de {self.montant} le {self.date_manquant} par {caissier_id}"