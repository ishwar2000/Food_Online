from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from accounts.models import user
from vendor.models import vendor
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
    Vendor = vendor.objects.get(user=request.user)
    print(vendor.vendor_name)
    context = {"user":request.user
               }
    return render(request, "vendor/vendorProfile.html", context)

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
        messages.info(request, "Logged out succesfully !!")
        logout(request)
    return render(request, "accounts/login.html")

@login_required(login_url='login')
def changePassword(request):
    request.session['uid'] = request.user.pk
    return render(request, "accounts/resetPassword.html",{"update":1})