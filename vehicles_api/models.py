# vehicles_api/models.py
from django.db import models

class VehicleType(models.Model):
    """
    Modèle représentant un Type de Véhicule (Catégorie).
    """
    label = models.CharField(max_length=100, unique=True, verbose_name="Libellé du Type")
    code = models.CharField(max_length=10, unique=True, verbose_name="Code Catégorie")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Type de Véhicule"
        verbose_name_plural = "Types de Véhicules"
        
    def __str__(self):
        return f"{self.code} - {self.label}"