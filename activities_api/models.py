# activities_api/models.py
from django.db import models
from django.conf import settings
# settings.AUTH_USER_MODEL référence CustomUser dans users_api.CustomUser
# N'oubliez pas d'importer le modèle User de votre application users_api si nécessaire

class Activity(models.Model):
    """
    Modèle représentant une Activité (par exemple, une action dans le système ou sur le terrain).
    """
    # L'activité est liée à l'utilisateur qui l'a effectuée
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Utilisateur"
    )
    title = models.CharField(max_length=255, verbose_name="Titre de l'activité")
    details = models.TextField(blank=True, null=True, verbose_name="Détails")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Horodatage")
    
    class Meta:
        verbose_name = "Activité"
        verbose_name_plural = "Activités"
        ordering = ['-timestamp'] # Tri par défaut : du plus récent au plus ancien
        
    def __str__(self):
        return f"Activité de {self.user.email if self.user else 'Inconnu'} : {self.title}"