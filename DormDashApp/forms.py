from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from models import User, Driver, Customer

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length = 15)
    delivery_address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','phone_number','delivery_address','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user

class DriverSignUpForm(UserCreationForm):
    ()


class EditProfileForm():
    ()

