# tarifs_api/models.py
from django.db import models
from sites_api.models import Site # Le tarif s'applique à un site

class Tarif(models.Model):
    """
    Modèle représentant un Tarif de péage.
    """
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Site/Tronçon Appliqué"
    )
    vehicle_type = models.CharField(
        max_length=50,
        choices=[
            ('C1', 'Classe 1 (Véhicules légers)'), 
            ('C2', 'Classe 2 (Intermédiaires)'), 
            ('C3', 'Classe 3 (Poids lourds 2 essieux)'),
            ('C4', 'Classe 4 (Poids lourds 3+ essieux)')
        ],
        verbose_name="Classe de Véhicule"
    )
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant du Tarif")
    is_active = models.BooleanField(default=True, verbose_name="Est Actif")
    start_date = models.DateField(verbose_name="Date d'Activation")
    
    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tarifs"
        # S'assurer qu'un type de véhicule n'a qu'un seul tarif actif par site
        unique_together = ('site', 'vehicle_type', 'is_active') 
        ordering = ['site__name', 'vehicle_type']
        
    def __str__(self):
        site_name = self.site.name if self.site else 'N/A'
        return f"Tarif {self.vehicle_type} - {self.montant} sur {site_name}"