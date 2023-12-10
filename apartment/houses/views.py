from django.shortcuts import render
from .models import HousesModel


def houses_home(request):
    houses= HousesModel.objects.order_by('-date')
    
    return render(request,'houses/houses_home.html',{'houses':houses})

def create_house(request):
    return render(request,'houses/create_house.html')