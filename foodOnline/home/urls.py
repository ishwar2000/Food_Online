
from django.urls import path, include
from .views import homePage, loginUser, logoutUser, customerDashboard, vendorDashboard, changePassword, restaurantProfile, marketPlace, restaurant

urlpatterns = [
    path('', homePage, name="homePage"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('customerDashboard/', customerDashboard, name="customerDashboard"),
    path('vendorDashboard/', vendorDashboard, name="vendorDashboard"),
    path('changePassword/', changePassword, name="changePassword"),
    path('restaurantProfile/', restaurantProfile, name="restaurantProfile"),
    path('marketPlace/', marketPlace, name="marketPlace"),
    path('restaurant/<id>', restaurant, name="restaurant")

]
