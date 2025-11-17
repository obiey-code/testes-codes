# get_vehicles_api/models.py

from django.db import models # Ligne 1: L'importation de base est obligatoire

class VehicleType(models.Model):
    # ... (Vos définitions de champs)
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du Type")
    code = models.CharField(max_length=10, unique=True, verbose_name="Code Court")
    description = models.TextField(blank=True, verbose_name="Description détaillée")
    
    class Meta:
        verbose_name = "Type de Véhicule"
        verbose_name_plural = "Types de Véhicules"
        ordering = ['code'] 

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    # ... (Vos définitions de champs)
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="Numéro d'Immatriculation")
    vehicle_type = models.ForeignKey(
        VehicleType, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='vehicles'
    )
    owner_name = models.CharField(max_length=255, blank=True, verbose_name="Nom du Propriétaire")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
        ordering = ['registration_number']

    def __str__(self):
        return self.registration_number