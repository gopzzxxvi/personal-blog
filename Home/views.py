from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def Signout(request):
    logout(request)
    return redirect("Home")

def HomePage(request):
    print(request.user.is_authenticated)
    return render(request, "Home.html")

def Signup(request):
    if(request.method == "POST"):
        Data = request.POST
        Display = request.POST.get('email', False)
        if(Display):
            User.objects.create_user(username=Data["username"], email=Data["email"], password=Data["password"])
            user = authenticate(username=Data["username"], password=Data["password"])
            login(request, user)
        else:
            user = authenticate(username=Data["username"], password=Data["password"])
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                return render(request, "Signup.html")
        return redirect("Home")
    else:
        if(request.user.is_authenticated):
            return redirect("Home")
        return render(request, "Signup.html")