from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from accounts.models import user, userProfile
from vendor.models import vendor
from django.contrib.auth.decorators import login_required, user_passes_test
from vendor.forms import registerVendorForm
from accounts.forms import userProfileForm
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
# Create your views here.
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied
    


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

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def restaurantProfile(request):
    Vendor = vendor.objects.get(user=request.user)
    UserProfile = userProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        vendor_form = registerVendorForm(request.POST, request.FILES, instance=Vendor)
        profile_form = userProfileForm(request.POST, request.FILES, instance=UserProfile)

        if vendor_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, "Profile Updated!")
            return redirect("restaurantProfile")
        else:
            print(profile_form.errors)
    else:
        vendor_form = registerVendorForm(instance=Vendor)
        profile_form = userProfileForm(instance=UserProfile)

    context = {"vendor_form" : vendor_form,
               "profile_form":profile_form,
               "profile":UserProfile}
    return render(request, "vendor/restaurant-restaurant.html", context)