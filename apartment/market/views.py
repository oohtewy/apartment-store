from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def home(request):
    return render(request,'market/home.html')


def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confpass = request.POST['confpass']

        if User.objects.filter(username=username):
            messages.error(request,'Username already exist!')
            return redirect('signup')
        
        if User.objects.filter(email= email):
            messages.error(request,'Email already exist!')
            return redirect('signup')
        
        if len(username)<2:
            messages.error(request, 'Your username must be longer than 2 characters')
            return redirect('signup')
            
        if  len(username)>50:
            messages.error(request, 'Your username must be shorter than 50 characters')
            return redirect('signup')
        
        if password != confpass:
            messages.error(request, 'Passwords did not match')
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-numeric')
            return redirect('signup/')
            

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, f'{fname} account has been successfully created') 
        return redirect('signin')
        
    
    
    return render(request, 'auth/signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name 
            messages.success(request, f'{fname} is logged succesfully') 
            return render(request, 'market/home.html', {'fname': fname})
        else:
            messages.error(request, 'Bad cridentials')
            return redirect('signin/')
    
    return render(request, 'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'You logged out successfuly')
    return redirect('home')

def about(request):
    return render(request,'market/about.html')
    
def contact(request):
    return render(request,'market/contact.html')
    