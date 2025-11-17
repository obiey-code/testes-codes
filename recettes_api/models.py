# recettes_api/models.py
from django.db import models
from caissiers_api.models import Caissier # Le caissier qui a effectué la transaction
from cabines_api.models import Cabine # La cabine où la transaction a eu lieu
from sites_api.models import Site # Le site de la transaction

class Recette(models.Model):
    """
    Modèle représentant un enregistrement de Recette (transaction d'encaissement).
    """
    caissier = models.ForeignKey(
        Caissier,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Caissier"
    )
    cabine = models.ForeignKey(
        Cabine,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Cabine"
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Site"
    )
    transaction_ref = models.CharField(max_length=100, unique=True, verbose_name="Référence Transaction")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant Encaissé")
    payment_method = models.CharField(
        max_length=20,
        choices=[('CASH', 'Espèces'), ('CARD', 'Carte'), ('SUBSCRIBER', 'Abonné')],
        default='CASH',
        verbose_name="Méthode de Paiement"
    )
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Horodatage")
    
    class Meta:
        verbose_name = "Recette"
        verbose_name_plural = "Recettes"
        ordering = ['-timestamp'] # Du plus récent au plus ancien
        
    def __str__(self):
        return f"Recette {self.transaction_ref} de {self.montant} par {self.caissier.matricule_caissier if self.caissier else 'N/A'}"