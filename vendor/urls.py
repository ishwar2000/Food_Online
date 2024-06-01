from django.urls import path, include
from .views import displayFoodItem, registerVendor, menuBuilder, addCategory, editCategory, deleteCategory, addFoodItem, editFoodItem, deleteFoodItem
urlpatterns = [
    path('registerVendor/', registerVendor, name="registerVendor" ),
    path('menuBuilder/', menuBuilder, name="menuBuilder" ),
    path('addCategory/', addCategory, name="addCategory" ),
    path('editCategory/<int:id>', editCategory, name="editCategory" ),
    path('deleteCategory/<int:id>', deleteCategory, name="deleteCategory" ),

    path('addFoodItem/', addFoodItem, name="addFoodItem" ),
    path('editFoodItem/<int:id>', editFoodItem, name="editFoodItem" ),
    path('deleteFoodItem/<int:id>', deleteFoodItem, name="deleteFoodItem" ),
    path('displayFoodItem/<int:id>',displayFoodItem,name="displayFoodItem")
]