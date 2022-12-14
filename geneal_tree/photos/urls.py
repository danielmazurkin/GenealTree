from .views import PhotoView
from django.urls import re_path


urlpatterns = [
    re_path(r'', PhotoView.as_view(), name='photo'),
]