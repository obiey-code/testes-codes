# cabines_api/models.py
from django.db import models
# Importation du modèle Site du package sites_api (nécessite l'ajout de sites_api à INSTALLED_APPS)
from sites_api.models import Site 

class Cabine(models.Model):
    """
    Modèle représentant une Cabine de Péage.
    """
    site = models.ForeignKey(
        Site, 
        on_delete=models.CASCADE, 
        verbose_name="Site Associé"
    )
    cabine_number = models.CharField(max_length=10, unique=True, verbose_name="Numéro de Cabine")
    direction = models.CharField(
        max_length=10, 
        choices=[('IN', 'Entrée'), ('OUT', 'Sortie')], 
        verbose_name="Direction"
    )
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Cabine"
        verbose_name_plural = "Cabines"
        # Assure l'unicité du numéro de cabine au sein du site (optionnel mais souvent nécessaire)
        unique_together = ('site', 'cabine_number')
        ordering = ['site__name', 'cabine_number']
        
    def __str__(self):
        return f"Cabine {self.cabine_number} ({self.site.name})"