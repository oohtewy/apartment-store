from django.shortcuts import render,redirect
from .models import HousesModel
from .forms import HousesForm
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required

@login_required
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


class HouseDetails(DetailView):
    queryset = HousesModel.objects.all()
    modal = HousesModel
    form_class = HousesForm
    template_name = 'houses/details_view.html'
    context_object_name ='house'
    

class HouseUpdate(UpdateView):
    queryset = HousesModel.objects.all()
    modal = HousesModel
    form_class = HousesForm
    template_name = 'houses/update_house.html'
 
class HouseDelete(DeleteView):
    queryset = HousesModel.objects.all()
    modal = HousesModel
    template_name = 'houses/delete_house.html'
    success_url='/houses/'







# class AddHouseView(CreateView):
#     modal = HousesModel
#     form_class = HousesForm
#     template_name = 'houses/create_house.html'
#     success_url = '/houses/'
    

#     def post(self, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             house = form.save(commit=False)
#             house.save()
#         return redirect('houses_home')

