from django.urls import path, include
from .views import registerVendor, menuBuilder, addCategory, editCategory
urlpatterns = [
    path('registerVendor/', registerVendor, name="registerVendor" ),
    path('menuBuilder/', menuBuilder, name="menuBuilder" ),
    path('addCategory/', addCategory, name="addCategory" ),
    path('editCategory/<int:id>', editCategory, name="editCategory" ),
    
]