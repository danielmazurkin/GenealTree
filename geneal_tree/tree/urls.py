"""general_tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users.views import UserView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('tree/', include('peoples.urls'), name='tree'),
    path('menu/', include('common.urls'), name='menu'),
    path('photo/', include('photos.urls'), name='photo'),
    path('bio/', include('bios.urls'), name='bio'),
    path('profiles/', include('profiles.urls'), name='profile'),
    path('users/', include('users.urls'), name='users_token'),
    path('register/', UserView.as_view(), name='user'),
]

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

