from django.shortcuts import render, redirect
from accounts.forms import registerUserForm
from .forms import registerVendorForm
from accounts.models import user, userProfile
from accounts.utils import send_verification_link
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