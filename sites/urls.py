# sites/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet

router = DefaultRouter()
# Enregistre le ViewSet : cela crée les routes /sites/, /sites/{pk}/ ET /sites/all/
router.register(r'sites', SiteViewSet, basename='site') 

urlpatterns = [
    # Inclut toutes les routes générées par le routeur
    path('', include(router.urls)),
]