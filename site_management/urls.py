# site_management/urls.py
from django.urls import path
from .views import SiteAllPostAPIView # Notez le nom de la nouvelle classe de vue

urlpatterns = [
    # Mappe 'sites/all' à notre vue
    path('sites/all', SiteAllPostAPIView.as_view(), name='site-all-post-list'),
]