

from django.urls import path
from .views import  HomePageView,CreateMobileObjectView


app_name = "mainsite"


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/mobile/', CreateMobileObjectView.as_view(), name='add_mobile'),
]
