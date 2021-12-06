from django.urls import include
from django.urls import path
from .v1 import urls as api_urls_v1


urlpatterns = [
    path('v1/', include((api_urls_v1, 'api_v1'))),
]
