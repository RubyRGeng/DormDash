from django.contrib.auth import login
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import redirect
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from DormDashApp.decorators import driver_required
from DormDashApp.models import Order


from DormDashApp.forms import DriverSignUpForm
from DormDashApp.models import User

class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('driver:driverorders')


@login_required
@driver_required
def OrderListView(ListView):
    model = Order
    
    driverorders = NullBooleanSelect
    order_list = get_object_or_404(driverorders, pk=pk)

  