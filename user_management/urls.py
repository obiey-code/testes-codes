# user_management/urls.py
from django.urls import path
from .views import UserSaveAPIView

urlpatterns = [
    # Mappe 'users/save' à notre vue
    path('users/save', UserSaveAPIView.as_view(), name='user-save'),
]