# vehicles_api/urls.py
from django.urls import path
from .views import VehicleTypeAllPostAPIView

urlpatterns = [
    # Mappe 'vehicle-types/all' à notre vue
    path('vehicle-types/all', VehicleTypeAllPostAPIView.as_view(), name='vehicle-type-all-list'),
]