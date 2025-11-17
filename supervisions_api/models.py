# supervisions_api/models.py
from django.db import models
from responsables_api.models import Responsable # Le responsable qui effectue l'audit
from sites_api.models import Site # Le site supervisé
from cabines_api.models import Cabine # La cabine spécifiquement auditée (optionnel)

class Supervision(models.Model):
    """
    Modèle représentant un événement de Supervision ou d'audit de haut niveau.
    """
    responsable = models.ForeignKey(
        Responsable,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Responsable Auditeur"
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Site Audité"
    )
    # Lier à la cabine est optionnel (peut être null si l'audit est général au site)
    cabine = models.ForeignKey(
        Cabine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Cabine Spécifique Auditée"
    )
    supervision_date = models.DateTimeField(verbose_name="Date et Heure de Supervision", auto_now_add=True)
    grade = models.CharField(
        max_length=20,
        choices=[('A', 'Excellent'), ('B', 'Bon'), ('C', 'Moyen'), ('D', 'Insatisfaisant')],
        default='A',
        verbose_name="Note d'Audit"
    )
    summary = models.TextField(verbose_name="Résumé de l'Audit")
    is_closed = models.BooleanField(default=False, verbose_name="Audit Clos")
    
    class Meta:
        verbose_name = "Supervision"
        verbose_name_plural = "Supervisions"
        ordering = ['-supervision_date'] # Du plus récent au plus ancien
        
    def __str__(self):
        responsable_id = self.responsable.matricule_responsable if self.responsable else 'N/A'
        site_name = self.site.name if self.site else 'N/A'
        return f"Supervision ({self.grade}) du {site_name} par {responsable_id}"