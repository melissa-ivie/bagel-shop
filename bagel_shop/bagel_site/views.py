from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, MenuItem
from random import randint

from django.core import serializers


# TODO: This is not actually how authentication will be handled. Just temporary until database stuff is working


# CONSTANTS -- NOTE: Might put these in their own module somewhere else if the list gets very big
RANDOM_PASSWORD_LENGTH = 12


def home(request):
    context = {
        "authenticated": request.user.is_authenticated, 
    }
    return render(request, 'home/home.html', context)


def order(request):

    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "bagels": serializers.serialize('json', MenuItem.objects.filter(item_type=0)),
        "spreads": serializers.serialize('json', MenuItem.objects.filter(item_type=1)),
        "toppings": serializers.serialize('json', MenuItem.objects.filter(item_type=2)),
        "drinks": serializers.serialize('json', MenuItem.objects.filter(item_type=3)),
    }

    return render(request, 'order/order.html', context)


def accounts_login(request):
    context = {
        'authenticated': False,
    }
    if request.method == "POST": 
        data = request.POST
        try: 
            username=data["email"]
            password=data["pwd"]
        except KeyError: 
            context["success"] = False
        else:
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                login(request, user)
                context["authenticated"] = True
                context["user"] = user
                context["success"] = True
                return HttpResponseRedirect(reverse('bagel_site:order')) 
            else: 
                context["success"] = False

    return render(request, 'accounts/login.html', context)

def accounts_logout(request):
    context = {
        'authenticated': True,
    }
    if request.method == "POST":
        logout(request)
        return render(request, 'accounts/login.html', context)


def accounts_create(request):
    context = {
        "authenticated": request.user.is_authenticated, 
        "user": request.user,
    }
    if request.method == "POST":
        # TODO Still assuming that input isn't garbage
        data = request.POST
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            cu = CustomUser.objects.create(user_base=User.objects.create_user(
                                                data["email"], # creating the user with username = email 
                                                data["email"], 
                                                data["pwd"],
                                                first_name=data["fname"],
                                                last_name=data["lname"]), phone_number=data["phone"]) 
            return HttpResponseRedirect(reverse('bagel_site:accounts-login')) 
        else:
            context["error"] = True

    return render(request, 'accounts/create.html', context)


def accounts_view(request):
    context = {
        'authenticated': False,
    }
    return render(request, 'accounts/view.html', context)


def accounts_edit(request):
    context = {
        "authenticated": request.user.is_authenticated, 
        "user": request.user,
    }
    return render(request, 'accounts/edit.html', context)


def accounts_reset_password(request):
    context = { 
        "reset_attempted":False, 
        "reset_successful":False
    }

    # if request is a POST to this endpoint we do the reset
    if request.method == "POST": 
        context["reset_attempted"] = True
        data = request.POST 

        # check if email exists in the database
        try: 
            u = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            pass 
        else:              
            context["reset_successful"] = True
            
            # randomly generate new password using ASCII values 
            new_password = ""
            for i in range(RANDOM_PASSWORD_LENGTH): 
                new_password += chr(randint(48,95))
            u.set_password(new_password) 
           
            # TODO Insert code to send email with temporary password here 
    return render(request, "accounts/password.html", context)





