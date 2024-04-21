from django.urls import path, include
from .views import registerVendor
urlpatterns = [
    path('registerVendor/', registerVendor, name="registerVendor" ),
    
]