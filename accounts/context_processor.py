from vendor.models import vendor
from home.models import userCart
def get_vendor(request):
    try:
        Vendor = vendor.objects.get(user=request.user) 
    except:
        Vendor = None
    
    return dict(vendor=Vendor)

def getCartItems(request):
    cartCout = 0

    if request.user.is_authenticated:
        try:
            currentCartItems = userCart.objects.filter(user=request.user)

            for item in currentCartItems:
                cartCout += item.quantity
        except:
            cartCout = 0
            
    return dict(cartCout=cartCout)

def getTotal(request):
    total = 0

    if request.user.is_authenticated:
        try:
            currentCartItems = userCart.objects.filter(user=request.user)
            # print(currentCartItems)
            for item in currentCartItems:
                # print(item)
                total += item.foodItem.price * item.quantity
        except:
            total = 0
        # print(total)
    return dict(subtotal=total, grand_total=total)