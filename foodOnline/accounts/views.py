from django.shortcuts import render, redirect
from .forms import registerUserForm
from .models import user
from django.contrib import messages
from .utils import send_verification_link, sendResetToken
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

def registerUser(request):
    if request.user.is_authenticated:
        return redirect("login")
    if request.method  == "POST":
        form = registerUserForm(request.POST)

        if form.is_valid():
            User = form.save(commit=False)
            User.role = user.Customer
            User.set_password(form.cleaned_data["password"])
            User.save()
            # send_verification
            send_verification_link(request, User)
            messages.info(request, "Account successfully registered, Please activate the account")
            return redirect("login")
    else:
        form = registerUserForm()
    return render(request, "accounts/registerUser.html", {'form' : form})

def resetPassword(request):
    pass

def activate(request, uid, token):
    try:
        pk =  urlsafe_base64_decode(uid).decode()
        User = user.objects.get(pk=pk)
    except:
        User = None
    
    if User is not None and default_token_generator.check_token(User, token):
        User.is_active = True
        User.save()
        messages.success(request, "Account succesfully activated")
        return redirect("login")
    else:
        messages.warning(request, "Activation failed")
    return redirect("login")

def forgotPassword(request):
    if request.method == "POST":
        email = request.POST["email"]

        try:
            User = user.objects.get(email=email)
        except:
            User = None
        
        if User is not None:
            sendResetToken(request, User)
            messages.success(request, "Sent token to your email")
        else:
            messages.warning(request, "Please register your account")

    return render(request, "accounts/forgotPassword.html")

def resetPassword(request):
    if request.method == "POST":
        password = request.POST["password"]
        confPassword = request.POST["confPassword"]
        if password != confPassword:
            messages.warning(request, "Password deos not match")
        else:
            uid =  request.session.get('uid')
            User = user.objects.get(pk=uid)
            User.set_password(password)
            User.save()
            messages.success(request, "Password Updated")
            return redirect("login")
    return render(request, "accounts/resetPassword.html")

def reset(request, uid, token):
    try:
        pk =  urlsafe_base64_decode(uid).decode()
        User = user.objects.get(pk=pk)
    except:
        User = None
    
    if User is not None and default_token_generator.check_token(User, token):
        request.session['uid'] = pk
        messages.info(request, 'Please reset your password')
        return redirect("resetPassword")
    else:
        messages.warning(request, "Token is not Valid")
    return redirect("forgotPassword")