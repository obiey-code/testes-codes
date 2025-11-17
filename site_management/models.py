# C:\Users\User\Desktop\Projet laravel vers django\API V1 DJANGO\site_management\models.py

from django.db import models

class Site(models.Model):
    """
    Modèle réutilisable pour représenter un site physique ou logique.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Nom du Site")
    code = models.CharField(max_length=50, unique=True, verbose_name="Code du Site (Identifiant court)")
    is_active = models.BooleanField(default=True, verbose_name="Est Actif")
    
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        ordering = ['name'] 

    def __str__(self):
        return f"{self.name} ({self.code})"