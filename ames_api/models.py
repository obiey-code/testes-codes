# ames_api/models.py
from django.db import models

class AME(models.Model):
    """
    Modèle représentant une entité d'Assistance à Maîtrise d'Ouvrage/Œuvre (AME).
    """
    code = models.CharField(max_length=50, unique=True, verbose_name="Code AME")
    name = models.CharField(max_length=150, verbose_name="Nom de l'Entité AME")
    contact_person = models.CharField(max_length=100, blank=True, null=True, verbose_name="Personne Contact")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "AME"
        verbose_name_plural = "AMES"
        ordering = ['name']
        
    def __str__(self):
        return f"{self.code} - {self.name}"