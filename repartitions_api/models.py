# repartitions_api/models.py
from django.db import models
from sites_api.models import Site # Le site où la répartition est effectuée

class Repartition(models.Model):
    """
    Modèle représentant une Répartition (distribution financière ou affectation de ressources).
    """
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Site de Répartition"
    )
    repartition_date = models.DateField(verbose_name="Date de Répartition")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant Réparti")
    category = models.CharField(
        max_length=50,
        choices=[('CASH', 'Espèces'), ('CARD', 'Carte'), ('OTHER', 'Autre')],
        default='CASH',
        verbose_name="Catégorie de Répartition"
    )
    details = models.TextField(blank=True, null=True, verbose_name="Détails")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Répartition"
        verbose_name_plural = "Répartitions"
        ordering = ['-repartition_date'] 
        
    def __str__(self):
        site_name = self.site.name if self.site else 'N/A'
        return f"Répartition de {self.montant} sur {site_name} le {self.repartition_date}"