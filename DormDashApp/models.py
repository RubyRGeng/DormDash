from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db.models.fields import NullBooleanField
from django.db import models
from django.contrib.auth.models import User

class menuItem(models.Model):
    pass

class Order(models.Model):
    resteraunt = models.CharField(max_length=100, null=True)
    items = models.ManyToManyField(menuItem)
    user = models.CharField(max_length = 100, null=True)
    
    def get_user(self):
        return NullBooleanField
    def get_items(self):
        return NullBooleanField
    def get_resteraunt(self):
        return NullBooleanField


class Customer(models.Model):
    email = models.CharField(max_length=200, null=True)  
    #username = models.CharField(max_length=200, null=True)  
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    #def get_username(self):
        #return NullBooleanField

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login

class Driver(models.Model):
    email = models.CharField(max_length=200, null=True)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    delivery_address = models.TextField()

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
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