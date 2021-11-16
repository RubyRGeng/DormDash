from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from DormDashApp.forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from DormDashApp.models import *

class SignUpView(TemplateView):
    template_name = 'createaccount.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_driver:
                return redirect('driverorders')
        else:
            return redirect('restaurant_list')

        return render(request, 'login.html')


@login_required
def logoutUser(request):
    logout(request)
    return redirect("/login")
    
@login_required(login_url='login')
def driverorders(request):
    return render(request, 'driverorders.html')


@login_required
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
