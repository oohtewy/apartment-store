from django.shortcuts import render

def houses_home(request):
    return render(request,'houses/houses_home.html')

def create_house(request):
    return render(request,'houses/create_house.html')