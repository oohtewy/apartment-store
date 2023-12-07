from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.houses_home,name='houses_home'),
]
