from .views import ProfileView
from django.urls import path


urlpatterns = [
    path('profile/<int:id>', ProfileView.as_view(), name='profile_view'),
]
