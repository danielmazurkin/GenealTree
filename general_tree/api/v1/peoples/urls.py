from django.urls import path
from .views import PeopleInfoView


urlpatterns = [
    path('', PeopleInfoView.as_view(), name='people_info_view'),
]
