from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.houses_home,name='houses_home'),
    path('create_house/', AddHouseView.as_view(),name='create_house'),
    path('<int:pk>', HouseDetails.as_view(),name='details'),
    path('<int:pk>/update', HouseUpdate.as_view(),name='update'),
    path('<int:pk>/delete', HouseDelete.as_view(),name='delete')
]
