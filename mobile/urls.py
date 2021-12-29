

from django.urls import path
from .views import  HomePageView,CreateMobileObjectView,DeleteProducts,Search_Phone


app_name = "mainsite"


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/mobile/', CreateMobileObjectView.as_view(), name='add_mobile'),
    path('delete/', DeleteProducts.as_view(), name='deleteitem'),
    path('search/', Search_Phone, name='search_phone')
]
