from django.contrib import admin
from django.urls import path, include
from .views import registerUser, activate, forgotPassword, resetPassword, reset
urlpatterns = [
    path('registerUser/', registerUser, name="registerUser" ),
    path('activate/<uid>/<token>/', activate, name="activate"),
    path("forgotPassword", forgotPassword, name="forgotPassword"),
    path("reset/<uid>/<token>", reset, name="reset"),
    path("resetPassword", resetPassword, name="resetPassword")
]