from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NullBooleanField


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

class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField()
    restaurant_pic = models.ImageField(upload_to='images/')

    def get_name(self):
        return self.name

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Restaurant._meta.fields]

    def upload_image(self, filename):
        return 'restaurant/{}/{}'.format(self.title, filename)


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    email = models.CharField(max_length=200, null=True)  
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=200, null=True)  
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    
    def __str__(self):
        return self.user.username

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username