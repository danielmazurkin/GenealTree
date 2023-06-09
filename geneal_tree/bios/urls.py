from .views import BioPeopleView
from django.urls import re_path


urlpatterns = [
    re_path(r'(?P<pk>\d+)/$', BioPeopleView.as_view(), name='bios'),
]