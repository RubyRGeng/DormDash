from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db.models.fields import NullBooleanField


class Customer(models.Model):
    email = models.EmailField(('email address'), unique=True)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    is_login = models.BooleanField(default=False)
    address = models.TextField()

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login

class Driver(models.Model):
    email = models.EmailField(('email address'), unique=True)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    is_login = models.BooleanField(default=False)
    delivery_address = models.TextField()

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login
        
'''
# Create your models here.
USER_TYPE = (
    (1, 'customer'),
    (2, 'driver'),
)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #email = models.EmailField(max_length=255)
    #email_verified = models.BooleanField(default=False)
    #activation_code = models.CharField(max_length=100, null=True, blank=True)
    #is_active = models.BooleanField(default=False)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    #user_type = models.CharField(choices=USER_TYPE, max_length=10)
    #is_admin = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)

    objects = UserManager

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()

    def get_deliveryAddress(self):
        return NullBooleanField

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    delivery_address = models.TextField()
'''