from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm

from .models import *
# Create your views here.
# request -> response
# request handle
# action

def createaccount(request):
    form = CustomerSignUpForm()
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context = {'form':form}
    return render(request, 'createaccount.html', context)
    
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
    return redirect("/login")
    
@login_required(login_url='login')
def driverorders(request):
    return render(request, 'driverorders.html')

def orderdetails(request):
    return render(request, 'orderdetails.html')

@login_required(login_url='login')
def restaurant_list(request):
    restaurantlist = Restaurant.objects.all()
    for x in restaurantlist:
        print(x.get_name)
    return render(request, 'restaurant_list.html',{'restaurantlist':restaurantlist })

@login_required
def profile(request):
    return render(request, 'profile.html')