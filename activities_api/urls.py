# activities_api/urls.py
from django.urls import path
from .views import ActivityListAPIView

# Le préfixe de cet app sera '/api/activities/'
urlpatterns = [
    # URL: /api/activities/list
    path('list', ActivityListAPIView.as_view(), name='activity-list'),
]