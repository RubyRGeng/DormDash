from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
# Create your views here.
# request -> response
# request handle
# action

def createaccount(request):
    form = CreateUserForm()
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'createaccount.html', context)

def login(request):
    #pull data from DB
    #Transform
    #Send Email
    return render(request, 'login.html')
def restaurant_list(request):
    #pull data from DB
    #Transform
    #Send Email
    return render(request, 'restaurant_list.html')