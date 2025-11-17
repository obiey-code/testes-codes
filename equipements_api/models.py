# equipements_api/models.py
from django.db import models
from cabines_api.models import Cabine # L'équipement est installé dans une Cabine

class Equipement(models.Model):
    """
    Modèle représentant un Équipement technique (e.g., barrière, lecteur de carte).
    """
    cabine = models.ForeignKey(
        Cabine,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Cabine d'Installation"
    )
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Numéro de Série")
    name = models.CharField(max_length=100, verbose_name="Nom de l'Équipement")
    status = models.CharField(
        max_length=20,
        choices=[('ONLINE', 'En Ligne'), ('OFFLINE', 'Hors Ligne'), ('MAINTENANCE', 'Maintenance')],
        default='OFFLINE',
        verbose_name="Statut"
    )
    last_check = models.DateTimeField(auto_now=True, verbose_name="Dernière Vérification")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Équipement"
        verbose_name_plural = "Équipements"
        ordering = ['serial_number']
        
    def __str__(self):
        return f"{self.name} ({self.serial_number})"