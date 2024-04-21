
from django.urls import path, include
from .views import homePage, loginUser, logoutUser, customerDashboard, vendorDashboard
urlpatterns = [
    path('', homePage, name="homePage"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('customerDashboard/', customerDashboard, name="customerDashboard"),
    path('vendorDashboard/', vendorDashboard, name="vendorDashboard"),
    

]
