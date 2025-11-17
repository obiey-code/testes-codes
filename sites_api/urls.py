# sites_api/urls.py
from django.urls import path
from .views import SiteListAPIView, SiteAllAPIView # Importer la nouvelle vue

# Le préfixe de cet app est '/api/sites/'
urlpatterns = [
    # URL: /api/sites/list (Avec pagination)
    path('list', SiteListAPIView.as_view(), name='site-list'),
    
    # URL: /api/sites/all (Sans pagination)
    path('all', SiteAllAPIView.as_view(), name='site-all'), 
]