from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.houses_home,name='houses_home'),
    path('create_house/', views.create_house,name='create_house'),
]
