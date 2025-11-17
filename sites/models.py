# sites/models.py (CODE CORRIGÉ)

from django.db import models
import uuid # <-- 1. Importer la bibliothèque standard

class Site(models.Model):
    """
    Modèle représentant un site de péage.
    """
    # 2. Utiliser uuid.uuid4 pour générer un UUID par défaut
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du Site")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Localisation")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    def __str__(self):
        return self.name