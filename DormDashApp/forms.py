from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from DormDashApp.models import Customer, Restaurant, User


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



class CustomerSignUpForm(UserCreationForm):

    email = forms.EmailField(required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )

    phone_number = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )
    
    address = forms.CharField(max_length=250,
                                    required=True,
                                    widget=forms.TextInput(attrs={'class': 'form-control'})
                                    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.email.add(*self.cleaned_data.get('email'))
        customer.phone_number.add(*self.cleaned_data.get('phone_number'))
        customer.address.add(*self.cleaned_data.get('address'))
        return user


class DriverSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit = True):
        user = super().save(commit=False)
        user.is_driver = True
        if commit:
            user.save()
        return user
        