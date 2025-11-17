# responsables_api/urls.py
from django.urls import path
from .views import ResponsableListAPIView

# Le préfixe de cet app sera '/api/responsables/'
urlpatterns = [
    # URL: /api/responsables/list
    path('list', ResponsableListAPIView.as_view(), name='responsable-list'),
]