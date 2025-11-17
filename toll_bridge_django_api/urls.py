# my_django_project/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # INTÉGRATION DU PACKAGE RÉUTILISABLE (APP)
    # Toutes les URLs dans auth_api/urls.py seront préfixées par 'api/auth/'
    path('api/auth/', include('auth_api.urls')),
    
    # Ajoutez ici les autres packages réutilisables :
    # path('api/toll-subscribers/', include('tolls_api.urls')),
    # path('api/users/', include('users_api.urls')),
    # ... autres chemins
    path('api/users/', include('users_api.urls')),
    # ... autres chemins
    path('api/sites/', include('sites_api.urls')),
    # ... autres chemins
    path('api/vehicle-types/', include('vehicles_api.urls')),
    # urls.py du projet principal
    path('api/activities/', include('activities_api.urls')),
    # ... autres chemins
    path('api/toll-subscribers/', include('tolls_api.urls')),
    # ... autres chemins
    path('api/agents/', include('agents_api.urls')),
    # ... autres chemins
    path('api/ames/', include('ames_api.urls')),
    # ... autres chemins
    path('api/cabines/', include('cabines_api.urls')),
    # ... autres chemins
    path('api/caissiers/', include('caissiers_api.urls')),
    # ... autres chemins
    path('api/controles/', include('controles_api.urls')),
    # ... autres chemins
    path('api/equipements/', include('equipements_api.urls')),
   
    # ... autres chemins
    path('api/manquants/', include('manquants_api.urls')),
    # ... autres chemins
    path('api/moneys/', include('moneys_api.urls')),
    # ... autres chemins
    path('api/recettes/', include('recettes_api.urls')),
    # ... autres chemins
    path('api/receveurs/', include('receveurs_api.urls')),
    # ... autres chemins
    path('api/repartitions/', include('repartitions_api.urls')),
    # ... autres chemins
    path('api/responsables/', include('responsables_api.urls')),
    # ... autres chemins
    path('api/suiveurs/', include('suiveurs_api.urls')),
    # ... autres chemins
    path('api/surveillances/', include('surveillances_api.urls')),
    # ... autres chemins
    path('api/supervisions/', include('supervisions_api.urls')),
    # ... autres chemins
    path('api/tarifs/', include('tarifs_api.urls')),
    # ...
    # L'URL finale sera : /api/users/save 
    path('api/user_management', include('user_management.urls')),
    path('api/site_management', include('site_management.urls')),
    path('api/vehicle_management', include('vehicle_management.urls')),
    path('api/get_vehicles_api', include('get_vehicles_api.urls')),
    # Incluez le package réutilisable sous le préfixe désiré
    path('api/', include('toll_users.urls')),

    # Vues de la documentation interactive
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # ...
    path('api/', include('sites.urls')), # Vos APIs pour les Sites sont maintenant sous /api/sites/
    # ...




]