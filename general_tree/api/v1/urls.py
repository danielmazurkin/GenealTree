from django.urls import include
from django.urls import path

api_urls = [
    path('peoples/', include('peoples.urls')),
]