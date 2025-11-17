# vehicles_api/urls.py
from django.urls import path
from .views import VehicleTypeAllAPIView

# Le préfixe de cet app sera '/api/vehicle-types/'
urlpatterns = [
    # URL: /api/vehicle-types/all
    path('all', VehicleTypeAllAPIView.as_view(), name='vehicle-type-all'),
]