from django.contrib import messages
from django.shortcuts import redirect, render 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def showLogin(request):
    
    return render(request,'login.html')


def autenticate(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
       
        user = authenticate(username=username, password=password)
        #result = User.objects.filter(is_superuser = 1)
        

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Si no esta autorizado envia error
            messages.error(request, 'Error: Login failed...')
            return render(request, "home.html")

    
def home(request):
    return render(request, 'home.html') 


def logout_view(request):
    logout(request)
    return render(request, 'home.html')