from vendor.models import vendor

def get_vendor(request):
    if request.user.is_authenticated:
        try:
            Vendor = vendor.objects.get(user=request.user) 
        except:
            Vendor = None
    else:
        Vendor = None
    return dict(vendor=Vendor)