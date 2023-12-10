from django.shortcuts import render,redirect
from .models import HousesModel
from .forms import HousesForm

def houses_home(request):
    houses= HousesModel.objects.order_by('-date')
    
    return render(request,'houses/houses_home.html',{'houses':houses})

def create_house(request):
    error=''
    if request.method =='POST':
        form= HousesForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save(commit=True)
            return redirect('houses_home')
        else:
            error='Form was Wrong'    
            
    form=HousesForm()
    context={
        'form':form,
        'error':error
    }
    return render(request,'houses/create_house.html',context)