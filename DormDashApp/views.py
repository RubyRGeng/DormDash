from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handle
# action

def createaccount(request):
    #pull data from DB
    #Transform
    #Send Email
    return render(request, 'createaccount.html')
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