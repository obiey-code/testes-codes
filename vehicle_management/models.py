# vehicles_api/models.py
from django.db import models

class VehicleType(models.Model):
    """
    Modèle réutilisable pour catégoriser les véhicules (ex: Classe 1, Classe 2, Moto).
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du Type")
    code = models.CharField(max_length=10, unique=True, verbose_name="Code Court")
    description = models.TextField(blank=True, verbose_name="Description détaillée")
    
    class Meta:
        verbose_name = "Type de Véhicule"
        verbose_name_plural = "Types de Véhicules"
        ordering = ['code'] 

    def __str__(self):
        return self.name