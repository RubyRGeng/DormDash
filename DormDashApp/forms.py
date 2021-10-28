from django.forms import ModelForm
from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_number = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email','phone_number']


class UpdateProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['address']

'''
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
'''
