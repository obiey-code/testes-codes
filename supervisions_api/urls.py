# supervisions_api/urls.py
from django.urls import path
from .views import SupervisionListAPIView

# Le préfixe de cet app sera '/api/supervisions/'
urlpatterns = [
    # URL: /api/supervisions/list
    path('list', SupervisionListAPIView.as_view(), name='supervision-list'),
]