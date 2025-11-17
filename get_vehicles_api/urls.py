# get_vehicles_api/urls.py

from django.urls import path
# L'importation doit être exacte pour éviter l'ImportError
from .views import VehicleTypeAllPostAPIView, VehicleRetrieveAPIView 

urlpatterns = [
    path('vehicle-types/all', VehicleTypeAllPostAPIView.as_view(), name='vehicle-type-all-list'),
    path('vehicles/<int:pk>', VehicleRetrieveAPIView.as_view(), name='vehicle-detail'),
]