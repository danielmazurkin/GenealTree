from .views import BioPeopleView
from django.urls import re_path


urlpatterns = [
    re_path(r'', BioPeopleView.as_view(), name='bios'),
]