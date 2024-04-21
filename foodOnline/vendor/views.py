from django.shortcuts import render
from accounts.forms import registerUserForm
from .forms import registerVendorForm
# Create your views here.
def registerVendor(request):
    if request.method == "POST":
        userForm = registerUserForm(request.POST)
        vendorForm = registerVendorForm(request.POST)

        if userForm.is_valid() and vendorForm.is_valid():
            User = userForm.save()
    else:
        userForm = registerUserForm()
        vendorForm = registerVendorForm()
    
    context = {
        'form':userForm,
        'vendorForm':vendorForm
    }
    return render(request, "vendor/registerVendor.html", context)