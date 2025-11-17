# sites_api/models.py
from django.db import models

class Site(models.Model):
    """
    Modèle représentant un Site dans le système.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du Site")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code Unique")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
        
    def __str__(self):
        return self.name