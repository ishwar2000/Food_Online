from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from accounts.models import user
from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse
# Create your views here.
def homePage(request):
    return render(request, "home/homePage.html")

@login_required(login_url='login')
def customerDashboard(request):
    user = request.user
    print(user)
    return HttpResponse("<h1>this is customerdashboard {{ user }}<h1>")

@login_required(login_url='login')
def vendorDashboard(request):
    return HttpResponse("<h1>this is vendorDashboard {{ request.user }}<h1>")

@login_required(login_url='login')
def checkAndRedirect(request):
    if request.user.role == user.Customer:
        return redirect("customerDashboard")
    elif request.user.role == user.Vendor:
        return redirect("vendorDashboard")
    return redirect("homePage")

def loginUser(request):
    if request.user.is_authenticated:
        return checkAndRedirect(request)
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password = password)

        if user is not None:
            messages.success(request,"login successfull")
            login(request, user)

            return checkAndRedirect(request)
        
        else:
            messages.warning(request,"login failed")
            

    return render(request, "accounts/login.html")

@login_required(login_url='login')
def logoutUser(request):
    if request.user.is_authenticated:
        print(request.user)
        logout(request)
    return render(request, "accounts/login.html")