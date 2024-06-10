
from django.urls import path, include
from .views import placeOrder,orderConfirm
urlpatterns = [
    path('placeOrder', placeOrder, name="placeOrder"),
    path('orderConfirm', orderConfirm, name="orderConfirm"),
    
]