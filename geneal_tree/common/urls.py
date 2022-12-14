from django.urls import re_path
from .views import CommonView

urlpatterns = [
    re_path(r'', CommonView.as_view())
]
