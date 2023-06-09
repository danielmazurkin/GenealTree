from django.urls import re_path
from .views import TreeView

urlpatterns = [
    re_path(r'(?P<pk>\d+)/$', TreeView.as_view(), name='tree')
]
