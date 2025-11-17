# surveillances_api/urls.py
from django.urls import path
from .views import SurveillanceListAPIView

# Le préfixe de cet app sera '/api/surveillances/'
urlpatterns = [
    # URL: /api/surveillances/list
    path('list', SurveillanceListAPIView.as_view(), name='surveillance-list'),
]