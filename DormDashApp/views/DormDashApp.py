from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'signup.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_driver:
                return redirect('drivers:driverorders')
        else:
            return redirect('restaurant_list')

        return render(request, 'login.html')

def createaccount(request):
    form = CreateUserForm()
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context = {'form':form}
    return render(request, 'createaccount.html', context)
    