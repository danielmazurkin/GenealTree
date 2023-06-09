from .views import PhotoView
from django.urls import re_path


urlpatterns = [
    re_path(r'(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
]