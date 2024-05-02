from django.shortcuts import render, redirect
from accounts.forms import registerUserForm
from .forms import registerVendorForm
from accounts.models import user, userProfile
from .models import vendor
from accounts.utils import send_verification_link
from menuBuilder.forms import CategoryForm
from menuBuilder.models import category 
from django.contrib.auth.decorators import login_required, user_passes_test
from home.views import check_role_vendor, check_role_customer
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your views here.

def registerVendor(request):
    if request.method == "POST":
        userForm = registerUserForm(request.POST)
        vendorForm = registerVendorForm(request.POST)

        if userForm.is_valid() and vendorForm.is_valid():
            User = userForm.save(commit=False)
            User.role = user.Vendor
            User.set_password(userForm.cleaned_data["password"])
            User.save()
            
            UserProfile = userProfile.objects.get(user=User)

            Vendor = vendorForm.save(commit=False)
            Vendor.user = User
            Vendor.userProfile = UserProfile
            Vendor.save()
            # send_verification
            send_verification_link(request, User)
            return redirect("login")
    else:
        userForm = registerUserForm()
        vendorForm = registerVendorForm()
    
    context = {
        'form':userForm,
        'vendorForm':vendorForm
    }
    return render(request, "vendor/registerVendor.html", context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menuBuilder(request):
    Vendor = vendor.objects.get(user=request.user)
    categories = category.objects.filter(vendor=Vendor)
    context = {"categories":categories}
    return render(request, "vendor/menuBuilder.html",context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def editCategory(request, id=None):
    currCategory = category.objects.get(pk=id)
    if request.method == "POST":
        editCategory = CategoryForm(request.POST, instance = currCategory)

        if editCategory.is_valid():
            editCategory.save()

            return redirect("menuBuilder")
    editCategory = CategoryForm(instance = currCategory)
    context = {"form":editCategory,"category":currCategory}
    return render(request, "vendor/editCategory.html",context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def addCategory(request):

    if request.method == "POST":
        AddCategory = CategoryForm(request.POST)
        
        if AddCategory.is_valid():
            category_name = AddCategory.cleaned_data["categoryName"]
            newCategory = AddCategory.save(commit=False)
            newCategory.vendor = vendor.objects.get(user = request.user)
            
            newCategory.save()
            newCategory.slug= slugify(category_name)+"-" +str(newCategory.id)
            newCategory.save()
            messages.success(request, "category Successfully created")
            return redirect("menuBuilder")
    else:
        AddCategory = CategoryForm()
    context = {"form":AddCategory}
    return render(request, "vendor/addCategory.html",context)