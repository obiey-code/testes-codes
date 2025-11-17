# tolls_api/models.py
from django.db import models
from django.conf import settings 
# settings.AUTH_USER_MODEL est CustomUser de notre app users_api

class TollSubscriber(models.Model):
    """
    Modèle représentant un Abonné au Péage.
    """
    # L'abonné pourrait être lié à un utilisateur de notre système (ex: client)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        verbose_name="Compte Utilisateur"
    )
    subscriber_number = models.CharField(max_length=50, unique=True, verbose_name="Numéro d'Abonné")
    registration_plate = models.CharField(max_length=20, unique=True, verbose_name="Plaque d'Immatriculation")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Solde Actuel")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Abonné au Péage"
        verbose_name_plural = "Abonnés au Péage"
        ordering = ['subscriber_number']
        
    def __str__(self):
        return self.subscriber_number