from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.
# request -> response
# request handle
# action

def createaccount(request):
    #pull data from DB
    #Transform
    #Send Email
    return render(request, 'createaccount.html')
def loginUser(request):
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("restaurant_list")
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'login.html')

#logout button: <a href="{% url 'logout' %}">Logout</a>

def logoutUser(request):
    logout(request)
    return redirect("")

@login_required(login_url='login')
def restaurant_list(request):
    #pull data from DB
    #Transform
    #Send Email
    return render(request, 'restaurant_list.html')